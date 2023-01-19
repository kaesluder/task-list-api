from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__, static_folder="../static", static_url_path="")
    CORS(app)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI"
        )
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI"
        )

    # Import models here for Alembic setup
    from app.models.task import Task
    from app.models.goal import Goal

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    import app.task_routes as task_routes

    app.register_blueprint(task_routes.bp)

    import app.goal_routes as goal_routes

    app.register_blueprint(goal_routes.bp)

    @app.route("/<path:filename>")
    def hello_world(filename):
        return send_from_directory("../static", filename)

    @app.route("/")
    def root_index():
        return send_from_directory("../static", "index.html")

    return app
