"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""

import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
@app.route("/")
def sitemap():
    return generate_sitemap(app)


@app.route("/members", methods=["GET"])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"family": members}

    return jsonify(response_body), 200


@app.route("/addMember", methods=["POST"])
def handle_adding():

    if "first_name" not in request.json:

        return jsonify({"error": "First name Not Found"})
    if "last_name" not in request.json:

        return jsonify({"error": "Last name Not Found"})
    if "age" not in request.json:

        return jsonify({"error": "Age Not Found"})
    if "lucky_numbers" not in request.json:

        return jsonify({"error": "Lucky Numbers Not Found"})

    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    age = request.json["age"]
    lucky_numbers = request.json["lucky_numbers"]

    member = {
        "id": jackson_family._generateId(),
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "lucky_numbers": lucky_numbers,
    }

    return jackson_family.add_member(member)


@app.route("/members/<int:memberId>", methods=["GET"])
def getMember(memberId):
    return jackson_family.get_member(memberId)

@app.route("/members/<int:memberId>", methods=["DELETE"])
def deleteMember(memberId):
    return jackson_family.delete_member(memberId)


# this only runs if `$ python src/app.py` is executed
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=PORT, debug=True)
