import logging
import os

from flask import Flask, request, jsonify

from database import db, db_repo
from my_service import super_service

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

file_handler = logging.FileHandler('rest_api.log')
logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(logger_formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


def not_found_error(msg):
    status_code = 404
    message = {
        'status': status_code,
        'message': msg
    }
    resp = jsonify(message)
    resp.status_code = status_code
    return resp


def sample_response(msg):
    status_code = 200
    message = {
        'status': status_code,
        'message': msg
    }
    resp = jsonify(message)
    resp.status_code = status_code
    return resp


@app.route("/microservice/", methods=["GET", "POST"])
def microservice_index():
    app.logger.info("Is this the real life? Or is this just fantasy?")
    return "Please use my service, this is how I get money"


@app.route("/microservice/add_test_users/<nb_of_users>", methods=["GET"])
def add_test_users(nb_of_users: int):
    nb_of_users = int(nb_of_users)

    for i in range(nb_of_users):
        db_repo.create_user("Test", "User{0}".format(i), "just{0}@test.com".format(i))

    app.logger.info("Test users are created")

    return sample_response("Created {0} test users".format(nb_of_users))


@app.route("/microservice/sample_service", methods=["POST"])
def use_sample_service():
    req_json = request.get_json()

    try:
        # For authentication
        api_key_str = req_json["api_key"]
        # For the service
        size = int(req_json["size"])
    except KeyError:
        app.logger.error("Could not find the necessary keys in the request's body")
        return not_found_error("Required keys are not found in POST's body")

    user = db_repo.find_user_by_api_key(api_key_str)

    if user is None:
        app.logger.error("No user found with {0} api key".format(api_key_str))
        return not_found_error("No associated user with this api key")

    if user.available_units < size:
        app.logger.error("User with api key {0} has no units to use the service".format(api_key_str))
        return not_found_error("Not enough unit to use the service")

    # Using the Sample Service
    random_str = super_service.generate_random_string(size)

    app.logger.info("Successful service usage by {0}".format(api_key_str))

    db_repo.update_after_service_usage(user, size)

    response_dict = {"service_result": random_str}

    return jsonify(response_dict)


if __name__ == '__main__':
    db.init_db()
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
