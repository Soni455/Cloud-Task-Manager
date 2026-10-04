import pytest

from app.main import app, tasks


@pytest.fixture(autouse=True)
def reset_tasks():
    tasks.clear()
    yield
    tasks.clear()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "running"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Docker"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["id"] == 1
    assert data["title"] == "Learn Docker"
    assert data["completed"] is False


def test_reject_empty_title(client):
    response = client.post(
        "/tasks",
        json={
            "title": ""
        }
    )

    assert response.status_code == 400


def test_update_task(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Old title"
        }
    )

    task_id = create_response.get_json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "title": "New title",
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["title"] == "New title"
    assert data["completed"] is True


def test_delete_task(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Delete me"
        }
    )

    task_id = create_response.get_json()["id"]

    response = client.delete(
        f"/tasks/{task_id}"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "task deleted"

    tasks_response = client.get("/tasks")

    assert tasks_response.get_json() == []