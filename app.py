from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "Basic Flask API"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    tasks.append(data)
    return {"message": "Task added"}

@app.route("/delete/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        return {"message": "Task deleted"}
    return {"error": "Invalid index"}

app.run(debug=True)