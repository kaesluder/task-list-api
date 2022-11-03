from flask import Blueprint
from app.models.task import Task 
from app import db
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("tasks", __name__, url_prefix="/tasks")

@bp.route("", methods=["GET"])
def handle_books_get():
    tasks = Task.query.all()

    tasks_list = []
    for t in tasks:
        tasks_list.append(t.to_dict())
    return jsonify(tasks_list)