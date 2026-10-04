from fastapi.testclient import TestClient

import config.settings as settings_mod
import chatbot.database as db_mod
import chatbot.service as service_mod


def test_health_and_chat(tmp_path, monkeypatch):
    db = tmp_path / "api.db"
    settings_mod.settings.db_path = str(db)
    settings_mod.settings.api_key = ""
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
    assert body["conversation_id"]
    feedback = client.post(
        "/feedback",
        json={"conversation_id": body["conversation_id"], "rating": "helpful"},
    )
    assert feedback.status_code == 200


def test_analytics_and_csv_export_are_aggregate_only(tmp_path):
    db = tmp_path / "analytics.db"
    settings_mod.settings.db_path = str(db)
    settings_mod.settings.api_key = ""
    db_mod.DB_PATH = str(db)
    service_mod._service = None

    from chatbot.database import init_db, save_feedback, save_message
    from src.api.app import app

    init_db()
    conversation_id = save_message(
        "private-user-message-never-export",
        "attraction_query|retrieval",
        "Visit the museum.",
    )
    assert save_feedback(conversation_id, "helpful")
    client = TestClient(app)

    analytics = client.get("/analytics", params={"days": 7})
    assert analytics.status_code == 200
    body = analytics.json()
    assert body["days"] == 7
    assert body["total_chat_turns"] == 1
    assert len(body["daily_volume"]) == 7
    assert sum(item["count"] for item in body["daily_volume"]) == 1
    assert any(item["count"] == 0 for item in body["daily_volume"])
    assert body["intent_counts"] == [{"name": "attraction_query", "count": 1}]
    assert body["source_counts"] == [{"name": "retrieval", "count": 1}]
    assert body["feedback_total"] == 1
    assert body["helpful_rate_pct"] == 100.0
    assert body["feedback_counts"] == [{"name": "helpful", "count": 1}]

    export = client.get("/analytics/export.csv", params={"days": 7})
    assert export.status_code == 200
    assert export.headers["content-type"].startswith("text/csv")
    assert 'filename="tourism-analytics.csv"' in export.headers["content-disposition"]
    assert export.text.startswith("date,metric,dimension,value")
    assert "attraction_query" in export.text
    assert "helpful_rate_pct" in export.text
    assert "private-user-message-never-export" not in export.text


def test_analytics_rejects_out_of_range_windows(tmp_path):
    db = tmp_path / "analytics-validation.db"
    settings_mod.settings.db_path = str(db)
    settings_mod.settings.api_key = ""
    db_mod.DB_PATH = str(db)
    service_mod._service = None

    from src.api.app import app

    client = TestClient(app)
    assert client.get("/analytics", params={"days": 0}).status_code == 422
    assert client.get("/analytics/export.csv", params={"days": 366}).status_code == 422


def test_feedback_updates_existing_vote_and_rejects_unknown_chat(tmp_path):
    db = tmp_path / "feedback.db"
    settings_mod.settings.db_path = str(db)
    settings_mod.settings.api_key = ""
    db_mod.DB_PATH = str(db)
    service_mod._service = None

    from src.api.app import app

    client = TestClient(app)
    chat = client.post("/chat", json={"message": "places to visit"})
    conversation_id = chat.json()["conversation_id"]
    payload = {"conversation_id": conversation_id, "rating": "helpful"}
    assert client.post("/feedback", json=payload).status_code == 200
    payload["rating"] = "not_helpful"
    assert client.post("/feedback", json=payload).status_code == 200

    analytics = client.get("/analytics").json()
    assert analytics["feedback_total"] == 1
    assert analytics["helpful_rate_pct"] == 0.0
    assert analytics["feedback_counts"] == [{"name": "not_helpful", "count": 1}]
    assert client.post(
        "/feedback", json={"conversation_id": 999999, "rating": "helpful"}
    ).status_code == 404
    assert client.post(
        "/feedback", json={"conversation_id": conversation_id, "rating": "bad"}
    ).status_code == 422


def test_analytics_uses_null_rate_until_feedback_arrives(tmp_path):
    db = tmp_path / "no-feedback.db"
    settings_mod.settings.db_path = str(db)
    settings_mod.settings.api_key = ""
    db_mod.DB_PATH = str(db)
    service_mod._service = None

    from src.api.app import app

    client = TestClient(app)
    body = client.get("/analytics").json()
    assert body["feedback_total"] == 0
    assert body["helpful_rate_pct"] is None
    export = client.get("/analytics/export.csv")
    assert ",feedback,helpful_rate_pct,\r\n" in export.text
