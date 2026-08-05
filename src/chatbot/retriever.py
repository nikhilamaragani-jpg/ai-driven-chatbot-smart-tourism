"""
Local RAG-style retriever over the tourism knowledge base.

Uses TF-IDF + cosine similarity (scikit-learn). This is an honest local
alternative to managed vector DBs / embedding APIs for portfolio demos.
Upgrade path: swap this module for FAISS/Chroma + embeddings without
changing the service layer contract.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .knowledge import KNOWLEDGE_BASE


@dataclass
class RetrievedChunk:
    key: str
    text: str
    score: float


class KnowledgeRetriever:
    def __init__(self, corpus: Optional[dict] = None) -> None:
        self.corpus = corpus or KNOWLEDGE_BASE
        self.keys: List[str] = list(self.corpus.keys())
        self.documents: List[str] = [f"{k}. {v}" for k, v in self.corpus.items()]
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(self.documents)

    def retrieve(self, query: str, top_k: int = 3) -> List[RetrievedChunk]:
        if not query or not query.strip():
            return []
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix).ravel()
        ranked = scores.argsort()[::-1][:top_k]
        chunks: List[RetrievedChunk] = []
        for idx in ranked:
            score = float(scores[idx])
            if score <= 0:
                continue
            key = self.keys[idx]
            chunks.append(
                RetrievedChunk(key=key, text=self.corpus[key], score=score)
            )
        return chunks

    def best_answer(self, query: str, min_score: float = 0.05) -> Tuple[Optional[str], List[RetrievedChunk]]:
        chunks = self.retrieve(query, top_k=3)
        if not chunks or chunks[0].score < min_score:
            return None, chunks
        # Compose a grounded answer from top snippets
        top = chunks[0]
        extras = [c.text for c in chunks[1:] if c.score >= min_score]
        answer = top.text
        if extras:
            answer = answer + " Related tip: " + extras[0]
        return answer, chunks


# Module-level singleton for app startup
_retriever: Optional[KnowledgeRetriever] = None


def get_retriever() -> KnowledgeRetriever:
    global _retriever
    if _retriever is None:
        _retriever = KnowledgeRetriever()
    return _retriever
