from flask import Flask,jsonify

app = Flask(__name__)

liga = ["junior","nacional","millonarios","medellin"]

@app.route("/")
def hello_world():
    return jsonify(liga)