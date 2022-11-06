import pytest
from app.slackbot import slackbot_post

@pytest.mark.skip(reason="Avoid spamming slack in development.")
def test_slackbot_post_success():
    """
    slackbot_post should return a tuple with 
    status, message. The message can be optionally
    passed to the user for slackbot api debugging.
    """

    # assign 
    text = "A test from python, pytest."

    # act
    status, results = slackbot_post(text)

    # assert
    assert status == True
    assert results["ok"] == True
    assert results["message"]["text"] == text

@pytest.mark.skip(reason="Avoid spamming slack in development.")
def test_slackbot_fail_on_no_text():
    """
    slackbot_post should return a tuple with 
    status, message. 
    """

    # assign 
    text = None

    # act
    status, results = slackbot_post(text)

    # assert
    assert status == False
    assert results["ok"] == False
