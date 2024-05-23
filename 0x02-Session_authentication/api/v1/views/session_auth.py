#!/usr/bin/env python3
"""
Module of Session Authentication
the file api/v1/views/session_auth.py, create a route POST
/auth_session/login (= POST /api/v1/auth_session/login):
"""

from api.v1.views import app_views
from flask import jsonify, request, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    from api.v1.app import auth  # Import auth only where needed

    # Retrieve email and password parameters from request form
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email is missing or empty
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Check if password is missing or empty
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Retrieve User instance based on the email
    users = User.search({"email": email})

    # If no User found, return 404 error
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    # If multiple users found, return 500 error
    if len(users) > 1:
        return jsonify({"error": "multiple users found for this email"}), 500

    user = users[0]  # Extract the single user from the list

    # If password is incorrect, return 401 error
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a Session ID for the User ID
    session_id = auth.create_session(user.id)

    # Return the dictionary representation of the User
    user_dict = user.to_json()

    # Set the cookie to the response
    response = make_response(jsonify(user_dict))
    response.set_cookie(os.environ.get('SESSION_NAME'), session_id)

    return response
