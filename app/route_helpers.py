from app import db
from app.models.task import Task
from flask import Blueprint, jsonify, abort, make_response, request


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