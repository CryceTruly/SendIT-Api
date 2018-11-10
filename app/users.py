from flask import Flask, jsonify, request, Response, json, Blueprint
from app.endpoints import parcels
import datetime
from validate_email_address import validate_email
import re

user_print = Blueprint('user_print', __name__)

@user_print.route('/api/v1/users', methods=['GET'])
def getall_users():
    return jsonify({"users": users}), 200


users = [
    {
        "user_id": 1,
        "fullname": "Cryce Truly",
        "username": "crycetruly",
        "phone_number": "+256756698765",
        "email": "shelan@gmail.com",
        "password": "14testwerek "

    }
    ,
    {
        "user_id": 2,
        "fullname": "Shearan King",
        "username": "sherah",
        "phone_number": "+256756698765",
        "email": "crycetruly@gmail.com",
        "password": "sherah ",
        "joined": datetime.datetime.now()

    },
    {
        "user_id": 3,
        "fullname": "Uncle Kiiza ",
        "username": "kw@gmail",
        "phone_number": "+256756698765",
        "email": "kwagala@gmail.com",
        "password": "14testwerek ",
        "joined": datetime.datetime.now()

    }
]


@user_print.route('/api/v1/users', methods=['POST'])
def create_user():
    """creates new user"""
    request_data = request.get_json()
    if not is_valid_user_request(request_data):
        return jsonify({"success": False, "msg": "Bad request"}), 400

    if not validate_email(request_data['email']):
        return jsonify({"success": False, "msg": "Email is badly formatted"}), 401
            

    
    for user in users:
        if user['email'] == request_data['email']:
            return jsonify({"success": False, "msg": "Email is already taken"}), 401
        if user['username'] == request_data['username']:
            return jsonify({"success": False, "msg": "Username is already taken"}), 401

        newuser = {
            "user_id": len(users) + 1,
            "fullname": request_data['fullname'],
            "username": request_data['username'],
            "phone_number": request_data['phone_number'],
            "email": request_data['email'],
            "password": request_data['password'],
            "joined": datetime.datetime.now()

        }

        users.append(newuser)
        return jsonify({"success": True, "user_id": newuser.get('user_id')}), 201
    


@user_print.route('/api/v1/users/<int:id>/parcels')
def get_user_parcels(id):
    user_parcels = []
    for parcel in parcels:
        if parcel['user_id'] == id:
            user_parcels.append(parcel)

    
    return jsonify({"user_parcel_orders": user_parcels, "count": len(user_parcels)}), 200


def is_valid_user_request(newuser):
    if "fullname" in newuser and "fullname" in newuser and "phone_number" in newuser and \
            "email" in newuser and "password" in newuser:
        return True
    else:
        return False


