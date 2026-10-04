from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
next_id = 1


@app.get("/")
def home():
    return jsonify({
        "service": "Cloud Task Manager API",
        "status": "running",
        "version": "1.0.0"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.get("/tasks")
def get_tasks():
    return jsonify(tasks)


@app.post("/tasks")
def create_task():
    global next_id

    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "title is required"
        }), 400

    task = {
        "id": next_id,
        "title": title.strip(),
        "completed": False
    }

    tasks.append(task)
    next_id += 1

    return jsonify(task), 201


@app.patch("/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json(silent=True) or {}

    for task in tasks:
        if task["id"] == task_id:

            if "title" in data:
                if not isinstance(data["title"], str) or not data["title"].strip():
                    return jsonify({
                        "error": "title must not be empty"
                    }), 400

                task["title"] = data["title"].strip()

            if "completed" in data:
                if not isinstance(data["completed"], bool):
                    return jsonify({
                        "error": "completed must be boolean"
                    }), 400

                task["completed"] = data["completed"]

            return jsonify(task)

    return jsonify({
        "error": "task not found"
    }), 404


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:

            deleted = tasks.pop(index)

            return jsonify({
                "message": "task deleted",
                "task": deleted
            })

    return jsonify({
        "error": "task not found"
    }), 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )