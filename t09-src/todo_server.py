# File: todo_server.py
from flask import Flask, jsonify, request
app = Flask(__name__)

# A list of dicts, e.g. { "id": 12, "desc": "Do work" }
todo = []

@app.get("/api/todos")
def get_all_todos():
    return jsonify(todo)

@app.delete("/api/todos/<int:id>")
def delete_todo(id):
    for i, item in enumerate(todo):
        if item["id"] == id:
            todo.pop(i)
            return jsonify({})
    return jsonify({"error": "todo item not found"}), 404

@app.post("/api/todos")
def create_todo():
    data = request.get_json()
    desc = data.get("desc")
    if not desc or not desc.strip():
        return jsonify({"error": "missing item desc"}), 400
    new_id = (max(item["id"] for item in todo) if todo else 0) + 1
    new_item = { "id": new_id, "desc": desc.strip() }
    todo.append(new_item)
    return jsonify(new_item)

if __name__ == "__main__":
    app.run()
