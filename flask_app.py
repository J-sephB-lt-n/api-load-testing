"""
docstring TODO
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# 3rd party imports #
import flask

app = flask.Flask(__name__)


@app.route("/log_user_in", methods=["POST"])
def log_user_in():
    """Logs a user in"""
    input_json: dict[str, str] = flask.request.get_json()
    user_name: str = input_json["user_name"]
    response = flask.make_response("OK")
    response.set_cookie(
        key="user_name",
        value=user_name,
    )
    logger.info("user %s logged in", user_name)
    return response


@app.route("/view_item/<item_name>", methods=["GET"])
def view_item(item_name: str):
    """Allows a user to view an item"""
    user_name: str = flask.request.cookies.get("user_name")
    if user_name is None:
        return flask.Response("Please Log In", status=401)
    logger.info("user %s viewed item %s", user_name, item_name)
    return flask.Response("OK", status=200)


@app.route("/add_item_to_basket", methods=["POST"])
def add_item_to_basket():
    """Allows a user to add an item to their basket"""
    user_name: str = flask.request.cookies.get("user_name")
    if user_name is None:
        return flask.Response("Please Log In", status=401)
    input_json: dict[str, str] = flask.request.get_json()
    item_name: str = input_json["item_name"]
    logger.info("user %s added item %s to their basket", user_name, item_name)
    return flask.Response("OK", status=200)
