"""
LangChain adapter (optional upgrade path).

This module documents the integration surface without requiring langchain
at install time for the default offline demo.

TODO (when upgrading):
1. pip install langchain langchain-community langchain-openai chromadb
2. Build RetrievalQA / create_retrieval_chain over tourism docs
3. Swap ChatService retrieval backend to LangChain retriever
"""

from __future__ import annotations

from typing import Any, Dict


def langchain_available() -> bool:
    try:
        import langchain  # noqa: F401

        return True
    except ImportError:
        return False


def describe_upgrade() -> Dict[str, Any]:
    return {
        "status": "optional_not_required_for_demo",
        "langchain_installed": langchain_available(),
        "recommended_stack": [
            "langchain",
            "langchain-openai or local embeddings",
            "chromadb or faiss",
            "FastAPI remains the HTTP layer",
        ],
        "note": (
            "Default portfolio demo uses TF-IDF/Hashing retrieval so recruiters "
            "can run without API keys. LangChain is the production orchestration path."
        ),
    }
