#!/usr/bin/env python3
""" App module
"""
from flask import Flask, jsonify, abort
from flask import request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Root path
    """
    reponse_payload = {
        "message": "Bienvenue"
    }
    return jsonify(reponse_payload)


@app.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """ Create a new user
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    message = {"email": email, "message": "user created"}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
