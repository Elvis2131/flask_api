from flask import Blueprint,request,jsonify
from src.database import User
import json

bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")

@bookmarks.route('/add_user', methods=['PUT'])
def insert_record():
    record = json.loads(request.data)
    user = User(username=record["username"],email=record["email"], password=record["password"])
    user.save()
    return jsonify(user.to_json())

@bookmarks.route('/update_user', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(username=record["username"]).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record["email"])
    return jsonify(user.to_json())