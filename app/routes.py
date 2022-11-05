from flask import Blueprint
from app.models.task import Task
from app import db
from app import route_helpers
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

    """
    Add a new record to the database via POST.

    Requires json request body.

    Returns json summary of new task object. 
    """


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

# DONE Get One Task: One Saved Task

@bp.route("/<id>", methods=["GET"])
def handle_single_task_record(id):

    book = route_helpers.validate_record_by_id(Task, id)
    return { "task": book.to_dict() }


# TODO Update Task


# ```json
# {
#   "title": "Updated Task Title",
#   "description": "Updated Test Description",
# }
# ```

# and get this response:

# `200 OK`

# ```json
# {
#   "task": {
#     "id": 1,
#     "title": "Updated Task Title",
#     "description": "Updated Test Description",
#     "is_complete": false
#   }
# }
# ```

@bp.route("/<id>", methods=["PUT"])
def update_book(id):
    task = route_helpers.validate_record_by_id(Task, id)

    request_body = request.get_json()

    task.title = request_body["title"]
    task.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify({"task": task.to_dict()}))



# TODO Delete Task: Deleting a Task
# TODO Create a Task: Invalid Task With Missing Data



# @books_bp.route("/<book_id>", methods=["PUT"])
# def update_book(book_id):
#     book = validate_model(Book, book_id)

#     request_body = request.get_json()

#     book.title = request_body["title"]
#     book.description = request_body["description"]

#     db.session.commit()

#     return make_response(jsonify(f"Book #{book.id} successfully updated"))

# @books_bp.route("/<book_id>", methods=["DELETE"])
# def delete_book(book_id):
#     book = validate_model(Book, book_id)

#     db.session.delete(book)
#     db.session.commit()

#     return make_response(jsonify(f"Book #{book.id} successfully deleted"))