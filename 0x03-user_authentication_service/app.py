#!/usr/bin/env python3
""" App module
"""
from flask import Flask, jsonify, abort
from flask import request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Root path
    """
    reponse_payload = {
        "message": "Bienvenue"
    }
    return jsonify(reponse_payload)


@app.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ Create a new user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        reponse_payload = {
            "email": email,
            "message": "user created"
        }
        return jsonify(reponse_payload)
    except Exception:
        reponse_payload = {
            "message": "email already registered"
        }
        return jsonify(reponse_payload), 400


@app.route('/sessions', methods=['POST'])
def log_in() -> str:
    """ Logs in a user and returns session ID """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    msg = {"email": email, "message": "logged in"}
    response = jsonify(msg)

    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
