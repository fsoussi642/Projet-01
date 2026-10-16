from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health(): assert client.get("/health").json()["status"]=="ok"
def test_create_task():
    r=client.post("/tasks",json={"title":"Documenter l'API"}); assert r.status_code==201 and r.json()["title"]=="Documenter l'API"
def test_invalid_task(): assert client.post("/tasks",json={"title":""}).status_code==422
