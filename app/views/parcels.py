from flask import jsonify, request, Blueprint
from app.model.parcel import Parcel
import re

ap = Blueprint('endpoint', __name__)
PARCEL = Parcel()


@ap.route("/")
def welcome():
    return jsonify({"message": "Welcome to the sendit api v1"}), 200


# GET parcels
@ap.route('/api/v1/parcels')
def get_parcels():
    '''
        returns a list of all order requests
    '''
    all = PARCEL.get_all_parcel()
    if all:
        return jsonify({'count': len(all), 'orders': all}), 200
    return jsonify({'msg': 'No parcel delivery orders posted yet', 'count': len(all)}), 404


# GET parcels/id
@ap.route('/api/v1/parcels/<int:id>')
def get_a_parcel(id):
    '''
    return order request details for a specific order
    '''
    if not PARCEL.is_parcel_exist(id):
        return jsonify({"msg": "parcel delivery request order not found"}), 404
    return jsonify(PARCEL.get_one_parcel(id)), 200


# POST /parcels
@ap.route('/api/v1/parcels', methods=['POST'])
def add_parcel():
    '''
    creates a new parcel order
    '''
    if not request.content_type == 'application/json':
        return jsonify({"failed": 'Content-type must be application/json'}), 415
    request_data = request.get_json()
    if not request.data is None:
        not_validresponse()

    if not PARCEL.is_valid_request(request_data):
        return not_validresponse()
    if not is_valid(request_data['sender_email']):
        return jsonify({"msg": "Sender email is invalid"}), 400
    if not is_valid(request_data['recipient_email']):
        return jsonify({"msg": "Recipient email is invalid"}), 400
    if len(str(request_data['recipient_phone'])) < 10:
        return jsonify({"msg": "Recipient Phone number should be atleast 10 characters"}), 400

    if len(str(request_data['comment_description'])) < 5:
        return jsonify({"msg": "Your Parcel description should be atleast 5 characters"}), 400
    if not isinstance(request_data['comment_description'], str):
        return jsonify({"msg": "Description should be string values"}), 400
    if not isinstance(request_data['pickup_address'], str):
        return jsonify({"msg": "pickup_address should be string values"}), 400

    if not isinstance(request_data['destination_address'], str):
        return jsonify({"msg": "destination_address should be string values"}), 400
    if not isinstance(request_data['status'], str):
        return jsonify({"msg": "current status should be string values"}), 400
    if not isinstance(request_data['weight'], int):
        return jsonify({"msg": "weight should be integer values"}), 400

    return PARCEL.add_parcel(request.get_json())


@ap.route('/api/v1/parcels/<int:id>/cancel', methods=['PUT'])
def cancel_parcel_request(id):
    '''
    cancels a specific request given its identifier
    '''
    if not 'user_id' in request.get_json():
        return jsonify({'msg': 'user_id is required'}), 400
    if not PARCEL.is_parcel_exist(id):
        return jsonify({"msg": "parcel delivery request not found"}), 404

    if PARCEL.is_order_delivered(id):
        return jsonify({"msg": "Not allowed parcel request has already been delivered"}), 403
    if not PARCEL.is_parcel_owner(request.get_json(), id):
        return jsonify({"msg": "You are not the parcel owner cannot cancel order"}), 403

    PARCEL.cancel_parcel(id)
    return jsonify(
        {"msg": "parcel request was cancelled successfully", "status": PARCEL.cancel_parcel(id).get("status"),
         "id": PARCEL.cancel_parcel(id).get("id")}), 200


@ap.route('/api/v1/parcels/<int:id>/changedest', methods=['PUT'])
def changedestination(id):
    '''
    changes destination address
    '''
    rdata = request.get_json()
    if not "destination_address" in rdata:
        return jsonify({'msg': 'Please add a new destination address'}), 415
    newdest = rdata['destination_address']
    if not PARCEL.is_parcel_exist(id):
        return jsonify({"msg": "parcel delivery request not found"}), 404
    if not PARCEL.is_parcel_exist(id):
        PARCEL.changedestination(newdest, id)
        return jsonify({'msg': 'updated successfully'}), 200
    else:
        return jsonify({'msg': 'order already delivered cant update'}), 403


def not_validresponse():
    '''
    helper to refactor similar response
    '''
    return jsonify({"error": 'Bad Request object,expected data is missing'}), 400


def is_should_update(data):
    if 'current_location' in data and 'status' in data:
        return True
    return False


def is_valid(email):
    """helper for checking valid emails"""

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True
