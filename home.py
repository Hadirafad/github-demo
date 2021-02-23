from flask import Flask, request, jsonify


@app.route("/", methods=['GET'])
def home():
    return "Welcome to Library Management Server"