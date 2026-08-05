from chatbot.retriever import KnowledgeRetriever


def test_retrieve_returns_relevant_chunks():
    r = KnowledgeRetriever()
    chunks = r.retrieve("visa requirements for travel", top_k=3)
    assert chunks
    assert any("visa" in c.key or "visa" in c.text.lower() for c in chunks)


def test_best_answer_not_empty_for_known_topic():
    r = KnowledgeRetriever()
    answer, chunks = r.best_answer("metro transport tips")
    assert answer is not None
    assert chunks
