#!/usr/bin/env python3
""" App module
"""
from flask import Flask, jsonify, abort
from flask import request, redirect
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


@app.route('/sessions', methods=['DELETE'])
def log_out() -> str:
    """  function to respond to the DELETE /sessions route.
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user_session = AUTH.get_user_from_session_id(session_id)

    if user_session is None:
        abort(403)

    AUTH.destroy_session(user_session.id)

    return redirect("/")


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """  function to respond to the GET /profile route.
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user_session = AUTH.get_user_from_session_id(session_id)

    if user_session is None:
        abort(403)

    return jsonify({"email": user_session.email}), 200


@app.route('/reset_password', methods=['POST'])
def reset_password() -> str:
    """  function to respond to the POST /reset_password route.
    """
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """  function to respond to the PUT /reset_password route.
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
