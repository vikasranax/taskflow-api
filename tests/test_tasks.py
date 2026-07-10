from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# TC-01: Create a task with valid data
def test_create_task_valid():
    response = client.post("/api/tasks", json={
        "title": "Buy groceries",
        "description": "Milk, eggs, bread"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Buy groceries"
    assert data["completed"] == False
    assert "id" in data


# TC-02: Get all tasks
def test_get_all_tasks():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# TC-03: Create task with empty title — this is a KNOWN BUG
# We write the test to match REALITY right now, and mark it clearly.
# Later, once we fix the bug, this test should be updated to expect a 422.
def test_create_task_empty_title_currently_allowed():
    response = client.post("/api/tasks", json={
        "title": "",
        "description": "test"
    })
    # documenting current (buggy) behavior — ideally this should be 422
    assert response.status_code == 200
    assert response.json()["title"] == ""


# TC-04: Update a task that doesn't exist — KNOWN BUG (wrong status code)
def test_update_nonexistent_task_returns_wrong_status():
    response = client.put("/api/tasks/9999", json={
        "title": "Doesn't exist",
        "description": "test"
    })
    # documenting current (buggy) behavior — ideally this should be 404
    assert response.status_code == 200
    assert response.json() == {"error": "Task not found"}


# TC-05: Delete a task that doesn't exist — same bug as TC-04
def test_delete_nonexistent_task_returns_wrong_status():
    response = client.delete("/api/tasks/9999")
    assert response.status_code == 200
    assert response.json() == {"error": "Task not found"}


# TC-06: task_id as text instead of a number — should fail validation
def test_update_task_with_invalid_id_type():
    response = client.put("/api/tasks/abc", json={
        "title": "test",
        "description": "test"
    })
    assert response.status_code == 422


# TC-07: Missing required field (description)
def test_create_task_missing_description():
    response = client.post("/api/tasks", json={
        "title": "No description"
    })
    assert response.status_code == 422
    body = response.json()
    assert body["detail"][0]["loc"] == ["body", "description"]


# TC-08: Extra/unexpected field — currently silently ignored
def test_create_task_with_extra_field_is_ignored():
    response = client.post("/api/tasks", json={
        "title": "Extra field test",
        "description": "test",
        "priority": "high"
    })
    assert response.status_code == 200
    assert "priority" not in response.json()


# Full lifecycle test — create, then update, then delete
def test_full_task_lifecycle():
    # create
    create_response = client.post("/api/tasks", json={
        "title": "Lifecycle test",
        "description": "test"
    })
    task_id = create_response.json()["id"]

    # update
    update_response = client.put(f"/api/tasks/{task_id}", json={
        "title": "Updated title",
        "description": "updated"
    })
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated title"

    # delete
    delete_response = client.delete(f"/api/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Task deleted"}