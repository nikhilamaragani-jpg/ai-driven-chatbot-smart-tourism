from fastapi.testclient import TestClient

import chatbot.database as db_mod
import chatbot.service as service_mod
import config.settings as settings_mod


def test_api_key_required_when_configured(tmp_path):
    db = tmp_path / "auth.db"
    settings_mod.settings.db_path = str(db)
    settings_mod.settings.api_key = "secret-demo"
    db_mod.DB_PATH = str(db)
    service_mod._service = None

    from src.api.app import app

    client = TestClient(app)
    denied = client.post("/chat", json={"message": "hello"})
    assert denied.status_code == 401

    ok = client.post(
        "/chat",
        json={"message": "hello"},
        headers={"X-API-Key": "secret-demo"},
    )
    assert ok.status_code == 200
    assert ok.json()["reply"]

    # reset
    settings_mod.settings.api_key = ""
