from flask import Blueprint
from app.models.task import Task
from app import db
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.route("", methods=["GET"])
def handle_tasks_list_get():
    """
    Endpoint: tasks
    Method: GET
    Returns a JSON list of all tasks in database.
    """

    tasks = Task.query.all()

    tasks_list = []
    for t in tasks:
        tasks_list.append(t.to_dict())
    return jsonify(tasks_list)


@bp.route("", methods=["POST"])
def handle_task_post():
    request_body = request.get_json()
    new_task = Task(
        title=request_body["title"],
        description=request_body["description"],
        completed_at=None,
    )

    db.session.add(new_task)
    db.session.commit()

    return_message = {}
    return_message["task"] = new_task.to_dict()

    return make_response(return_message, 201)
