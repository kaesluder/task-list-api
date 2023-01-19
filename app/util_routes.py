from flask import Blueprint
from app.models.task import Task
from app import db
from app import route_helpers
from flask import Blueprint, jsonify, abort, make_response, request
from datetime import datetime
from app.slackbot import slackbot_post

bp = Blueprint(
    "util",
    __name__,
    url_prefix="/static",
    static_url_path="/static",
    static_folder="static",
)
