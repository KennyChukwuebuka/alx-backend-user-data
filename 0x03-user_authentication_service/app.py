#!/usr/bin/env python3
""" App module
"""
from flask import Flask, jsonify
from flask import request
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=True)
def root_path():
    """ Root path
    """
    reponse_message = {
        "message": "Bienvenue"
    }
    return jsonify(reponse_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
