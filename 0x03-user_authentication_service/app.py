#!/usr/bin/env python3
""" App module
"""
from flask import Flask, jsonify
from flask import request


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Root path
    """
    reponse_payload = {
        "message": "Bienvenue"
    }
    return jsonify(reponse_payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
