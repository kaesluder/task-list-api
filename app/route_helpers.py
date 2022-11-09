from app import db
from app.models.task import Task
from flask import Blueprint, jsonify, abort, make_response
from requests import HTTPError


def validate_record_by_id(cls, id):
    """
    Tries to fetch a record from the database using
    primary key id.

    Takes: class of model and id of record

    Returns record to the calling function on success.
    Calls abort and sends JSON to client on failure.
    """

    try:
        id = int(id)
    except:
        abort(make_response(jsonify({"message": f"{cls.__name__} {id} invalid"}), 400))

    record = cls.query.get(id)

    if not record:
        abort(
            make_response(jsonify({"message": f"{cls.__name__} {id} not found"}), 404)
        )

    return record


def validate_json_data(request, required_fields):
    """
    Validates json from a request object checking for
    required_fields.

    Delivers 400 code and error to users on failure.
    Returns data dict to calling function on success.
    """

    try:
        request_data = request.get_json()
        missing_fields = []
        for f in required_fields:
            if not request_data.get(f):
                missing_fields.append(f)

        if missing_fields:
            raise HTTPError(f"Missing required fields: {missing_fields}.")

        return request_data

    # This block catches the HTTPError, as well as json = "foo" or json = []
    except Exception as e:
        abort(
            make_response(
                jsonify({"message": f"Something went wrong parsing your request: {e}"}),
                400,
            )
        )
