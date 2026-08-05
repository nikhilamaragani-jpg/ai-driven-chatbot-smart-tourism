from fastapi.testclient import TestClient

import config.settings as settings_mod
import chatbot.database as db_mod
import chatbot.service as service_mod


def test_health_and_chat(tmp_path, monkeypatch):
    db = tmp_path / "api.db"
    settings_mod.settings.db_path = str(db)
    db_mod.DB_PATH = str(db)
    service_mod._service = None

    from src.api.app import app

    client = TestClient(app)
    h = client.get("/health")
    assert h.status_code == 200
    assert h.json()["status"] == "ok"

    r = client.post("/chat", json={"message": "budget planning tips"})
    assert r.status_code == 200
    body = r.json()
    assert "reply" in body
    assert body["reply"]
