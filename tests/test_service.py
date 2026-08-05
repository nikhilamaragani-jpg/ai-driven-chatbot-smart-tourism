import os
from pathlib import Path

import pytest

# Isolate DB for tests
@pytest.fixture(autouse=True)
def _tmp_db(tmp_path, monkeypatch):
    db = tmp_path / "test_chat.db"
    monkeypatch.setenv("DB_PATH", str(db))
    # reset settings + service singletons
    import config.settings as settings_mod
    import chatbot.database as db_mod
    import chatbot.service as service_mod

    settings_mod.settings.db_path = str(db)
    db_mod.DB_PATH = str(db)
    service_mod._service = None
    yield


def test_chat_returns_reply():
    from chatbot.service import ChatService

    svc = ChatService()
    result = svc.chat("hello")
    assert result.reply
    assert result.intent
    assert result.source in {"retrieval", "intent_template"}


def test_history_after_chat():
    from chatbot.service import ChatService

    svc = ChatService()
    svc.chat("places to visit")
    rows = svc.history(5)
    assert len(rows) >= 1
