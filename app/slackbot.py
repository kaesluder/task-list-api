import requests
import dotenv
import os
from flask import jsonify

dotenv.load_dotenv()


def slackbot_post(text):
    """
    Post text to slack return tuple with status and
    returned fields from slack.
    """

    # REVIEW: Make asynch?

    # DONE: setup error checking for environ import.
    auth_token = "Bearer " + str(os.environ.get("SLACKBOT_TOKEN"))
    channel = os.environ.get("SLACKBOT_CHANNEL")
    endpoint = os.environ.get("SLACKBOT_ENDPOINT")

    if not (auth_token and channel and endpoint):
        return (False, {"ok": False, "message": "Slackbot disabled for testing."})

    # hack to avoid spamming slack during development.
    # PONY figure out way to set up dummy request/response objects.
    testing = os.environ.get("SLACKBOT_DISABLED")
    if testing == "YES":
        return (False, {"ok": False, "message": "Slackbot disabled for testing."})

    request_body = {"channel": channel, "text": text}

    headers = {"Authorization": auth_token, "Content-Type": "application/json"}

    response = requests.post(endpoint, json=request_body, headers=headers)

    # throw a more helpful exception if the request fails
    # if requests.get fails, bad data can get passed
    # downstream.
    if response.status_code != 200:
        raise requests.HTTPError(f"{response.status_code}: {response.reason}")

    # return the formatted data
    response_data = response.json()
    response_status = response_data.get("ok", False)
    return (response_status, response_data)
