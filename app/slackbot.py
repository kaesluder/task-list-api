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

    # REVIEW: setup error checking for environ import.
    auth_token = "Bearer " + os.environ["SLACKBOT_TOKEN"]
    channel = os.environ["SLACKBOT_CHANNEL"]
    endpoint = os.environ["SLACKBOT_ENDPOINT"]

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
