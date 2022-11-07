from flask import Blueprint
from app.models.goal import Goal
from app import db
from app import route_helpers
from flask import Blueprint, jsonify, abort, make_response, request
from datetime import datetime
from app.slackbot import slackbot_post

bp = Blueprint("goals", __name__, url_prefix="/goals")


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

    goal_query = Goal.query

    # set sort order
    # REVIEW Consider moving sort logic to anothr function.

    sort_order = args.get("sort")

    if sort_order == "asc":
        goals = goal_query.order_by(Goal.title.asc())
    elif sort_order == "desc":
        goals = goal_query.order_by(Goal.title.desc())
    else:
        goals = goal_query.all()

    goals_list = [t.to_dict() for t in goals]
    return jsonify(goals_list)


@bp.route("", methods=["POST"])
def handle_goal_post():
    """
    Add a new record to the database via POST.

    Requires json request body.

    Returns json summary of new goal object.
    Returns 400 status and json summary on error.
    """

    request_body = request.get_json()

    # error checking

    if "title" not in request_body:
        abort(make_response(jsonify({"details": "Invalid data"}), 400))

    new_goal = Goal(
        title=request_body["title"]
    )

    print(new_goal.to_dict)

    db.session.add(new_goal)
    db.session.commit()

    return_message = {}
    return_message["goal"] = new_goal.to_dict()

    return make_response(return_message, 201)


@bp.route("/<id>", methods=["GET"])
def handle_single_goal_record(id):
    """
    Fetches a single goal record by id.

    Returns: json summary of goal on success.
    Error: 404 or 400 response with json summary.
    """

    goal = route_helpers.validate_record_by_id(Goal, id)
    return {"goal": goal.to_dict()}


@bp.route("/<id>", methods=["PUT"])
def update_goal(id):
    """
    Update goal.title and/or goal.body by id.
    Does not update goal.completed_at.

    Returns: 200 and json body of updated record.
    Error: 404 or 400 and json body.
    """
    # REVIEW Docstrings.

    goal = route_helpers.validate_record_by_id(Goal, id)

    request_body = request.get_json()

    goal.title = request_body["title"]

    db.session.commit()

    return make_response(jsonify({"goal": goal.to_dict()}))



@bp.route("/<id>", methods=["DELETE"])
def delete_goal(id):
    """
    Delete goal.title and/or goal.body by id.

    Returns: 200 and json containing goal.id and goal.title.
    Error: 404 or 400 and json body.
    """

    goal = route_helpers.validate_record_by_id(Goal, id)

    db.session.delete(goal)
    db.session.commit()

    return make_response(
        jsonify({"details": f'Goal {goal.id} "{goal.title}" successfully deleted'})
    )

