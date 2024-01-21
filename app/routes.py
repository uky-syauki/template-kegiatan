from flask import jsonify
from app import app
from app.models import BphCoconut


@app.route("/")
def index():
    return "Hello World"


@app.route("/api/profile/<nra>", methods=["GET"])
def geProfile(nra):
    try:
        data = BphCoconut.query.filter_by(nra=nra).first()
        data = {
            "nama_lengkap": data.nama_lengkap,
            "urlImg": data.profile,
            "kampus": data.kampus
        }
        return jsonify(data)
    except:
        data = {
            "nama_lengkap": "Tidak di kenal",
            "urlImg": "",
            "kampus": ""
        }
        return jsonify(data)
    

@app.route("/api/bphlist", methods=["GET"])
def bphlist():
    data = BphCoconut.query.order_by(BphCoconut.nra.asc()).all()
    newdata = []
    for isi in data:
        newdata.append([isi.nama_lengkap, isi.profile, isi.nra, isi.depart])
    return jsonify(newdata)


@app.route("/api/getdata", methods=["GET"])
def getData():
    return jsonify({"nama": "Fauzan", "usia":23})