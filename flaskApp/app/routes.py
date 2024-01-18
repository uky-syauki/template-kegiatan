from flask import jsonify
from app import app



@app.route("/")
def index():
    return "Hello World"


@app.route("/api/getdata", methods=["GET"])
def getData():
    return jsonify({"nama": "Fauzan", "usia":23})