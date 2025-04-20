from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
import time



app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
db = client["passover_db"]
collection = db["names"]

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')


    if not first_name or not last_name:
        return jsonify({"error": "Missing first or last name"}), 400

    collection.insert_one({"first_name": first_name, "last_name": last_name})
    return jsonify({"message": "Name added successfully!"})


@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {'_id': 0}))
    return jsonify(users)


@app.route('/')
def home():
    return "Welcome to the Passover Name API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
