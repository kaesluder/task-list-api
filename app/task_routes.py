from flask import Blueprint
from app.models.task import Task
from app import db
from app import route_helpers
from flask import Blueprint, jsonify, abort, make_response, request
from datetime import datetime
from app.slackbot import slackbot_post

bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.route("", methods=["GET"])
def handle_tasks_list_get():
    """
    Endpoint: tasks
    Method: GET
    Returns a JSON list of all tasks in database.

    Default sort order is by id. If sort is in requets.args
    sort alphabetically by title. (asc or desc)
    """

    args = request.args

    task_query = Task.query

    # set sort order
    # REVIEW Consider moving sort logic to anothr function.

    sort_order = args.get("sort")

    if sort_order == "asc":
        tasks = task_query.order_by(Task.title.asc())
    elif sort_order == "desc":
        tasks = task_query.order_by(Task.title.desc())
    else:
        tasks = task_query.all()

    tasks_list = [t.to_dict() for t in tasks]
    return jsonify(tasks_list)


@bp.route("", methods=["POST"])
def handle_task_post():

    """
    Add a new record to the database via POST.

    Requires json request body.

    Returns json summary of new task object.
    Returns 400 status and json summary on error.
    """

    request_body = route_helpers.validate_json_data(request, ["title", "description"])

    new_task = Task(
        title=request_body["title"], description=request_body["description"]
    )

    print(new_task.to_dict)

    db.session.add(new_task)
    db.session.commit()

    return_message = {}
    return_message["task"] = new_task.to_dict()

    return make_response(return_message, 201)


# DONE Get One Task: One Saved Task


@bp.route("/<id>", methods=["GET"])
def handle_single_task_record(id):
    """
    Fetches a single task record by id.

    Returns: json summary of task on success.
    Error: 404 or 400 response with json summary.
    """

    task = route_helpers.validate_record_by_id(Task, id)
    return {"task": task.to_dict()}


# DONE Update Task


@bp.route("/<id>", methods=["PUT"])
def update_task(id):
    """
    Update task.title and/or task.body by id.
    Does not update task.completed_at.

    Returns: 200 and json body of updated record.
    Error: 404 or 400 and json body.
    """
    # REVIEW Docstrings.

    task = route_helpers.validate_record_by_id(Task, id)

    request_body = route_helpers.validate_json_data(request, ["title", "description"])

    task.title = request_body["title"]
    task.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify({"task": task.to_dict()}))


# DONE Delete Task: Deleting a Task


@bp.route("/<id>", methods=["DELETE"])
def delete_task(id):
    """
    Delete task.title and/or task.body by id.
    Does not update task.completed_at.

    Returns: 200 and json containing task.id and task.title.
    Error: 404 or 400 and json body.
    """

    task = route_helpers.validate_record_by_id(Task, id)

    db.session.delete(task)
    db.session.commit()

    return make_response(
        jsonify({"details": f'Task {task.id} "{task.title}" successfully deleted'})
    )


### DONE Mark Complete on an Incompleted Task
### DONE Mark Incomplete on a Completed Task
### DONE Mark Complete on a Completed Task
### DONE Mark Incomplete on an Incompleted Task
### DONE Mark Complete and Mark Incomplete for Missing Tasks


@bp.route("/<id>/mark_<mark>", methods=["PATCH"])
def mark_task_complete_incomplete(id, mark):
    """
    Modifies a record to add or remove timestamp from
    task.completed at.

    Returns dict of modified record on success.
    Returns 400 or 404 on failure, including an invalid
    mark. ("/task/id/mark_hamil", not valid for this
    db at least.)

    """

    # Error Check: if the mark is *not* complete or incomplete,
    # stop processing and return 400 status to client.
    if mark not in {"complete", "incomplete"}:
        abort(make_response(jsonify({"message": f"mark_{mark} invalid"}), 400))

    # grab the existing task, validate_record returns 400 or 404 if
    # given bad input.
    task = route_helpers.validate_record_by_id(Task, id)

    if mark == "complete":
        dt = datetime.now()
        task.completed_at = dt

        slack_status, slack_result = slackbot_post(f"{task.title} marked complete.")

        # dump slack debug info to stdout for now.
        # not sure how to test this branch further.
        if not slack_status:
            print("Slack post failed:")
            print(slack_result)

    elif mark == "incomplete":
        task.completed_at = None

    db.session.commit()
    return make_response(jsonify({"task": task.to_dict()}), 200)
