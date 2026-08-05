"""
Vector-store style interface for tourism knowledge.

Default backend: TF-IDF / hashing vectors (offline, no API key).
Upgrade path: implement ChromaStore / FAISSStore with real embeddings.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Sequence

import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .knowledge import KNOWLEDGE_BASE


@dataclass
class VectorHit:
    doc_id: str
    text: str
    score: float


class VectorStore(ABC):
    @abstractmethod
    def similarity_search(self, query: str, k: int = 3) -> List[VectorHit]:
        raise NotImplementedError


class HashingVectorStore(VectorStore):
    """Lightweight local embedding-like store for portfolio demos."""

    def __init__(self, corpus: Optional[dict] = None, n_features: int = 2**12) -> None:
        self.corpus = corpus or KNOWLEDGE_BASE
        self.ids: List[str] = list(self.corpus.keys())
        self.texts: List[str] = [f"{k}. {v}" for k, v in self.corpus.items()]
        self.vectorizer = HashingVectorizer(
            n_features=n_features,
            alternate_sign=False,
            norm="l2",
            stop_words="english",
        )
        self.matrix = self.vectorizer.transform(self.texts)

    def similarity_search(self, query: str, k: int = 3) -> List[VectorHit]:
        if not query.strip():
            return []
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix).ravel()
        order = np.argsort(scores)[::-1][:k]
        hits: List[VectorHit] = []
        for idx in order:
            score = float(scores[idx])
            if score <= 0:
                continue
            doc_id = self.ids[idx]
            hits.append(VectorHit(doc_id=doc_id, text=self.corpus[doc_id], score=score))
        return hits


class ChromaStorePlaceholder(VectorStore):
    """TODO: wire chromadb + real embeddings when OPENAI_API_KEY or local model is available."""

    def similarity_search(self, query: str, k: int = 3) -> List[VectorHit]:
        raise NotImplementedError(
            "ChromaStore is a roadmap item. Use HashingVectorStore for offline demos."
        )


def get_default_vector_store() -> VectorStore:
    return HashingVectorStore()
