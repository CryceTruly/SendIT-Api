from flask import jsonify, request, Response, json, Blueprint

import datetime

ap = Blueprint('endpoint', __name__)
parcels = []


# GET parcels
@ap.route('/api/v1/parcels')
def get_parcels():
    '''
    returns a list of all requests
    '''
    if len(parcels) == 0:
        return jsonify({'msg': 'No parcels yet'}), 200
    return jsonify({'parcels': parcels, 'count': len(parcels)}), 200


# GET parcels/id
@ap.route('/api/v1/parcels/<int:id>')
def get_a_parcel(id):
    '''
    return order request details for a specific order
    '''
    theparcel = []
    for parcel in parcels:
        if parcel['id'] == id:
            theparcel.append(parcel)
    if len(theparcel) == 0:
        return jsonify({"msg": "parcel delivery request not found"}), 404
    return jsonify(theparcel[0]), 200


# POST /parcels
@ap.route('/api/v1/parcels', methods=['POST'])
def add_parcel():
    '''
    creates a new parcel order
    '''

    if not request.content_type == 'application/json':
        return jsonify({"failed": 'Content-type must be application/json'}), 401
    request_data = request.get_json()
    if is_valid_request(request_data):
        parcel = {
            'id': len(parcels) + 1,
            'pickup_address': request_data['pickup_address'],
            'destination_address': request_data['destination_address'],
            'comment_description': request_data['comment_description'],
            'status': request_data['status'],
            'current_location': request_data['current_location'],
            'created': datetime.datetime.now(),
            'user_id': request_data['user_id'],
            'recipient_address': request_data['recipient_address'],
            'recipient_phone': request_data['recipient_phone'],
            'recipient_email': request_data['recipient_email']
        }
        parcels.append(parcel)
        response = Response(response=json.dumps({
            'msg': "Parcel delivery successfully created", 'request_id':
            parcel.get('id')}),
            status=201, mimetype="application/json")
        response.headers['Location'] = "parcels/" + str(parcel['id'])
        return response
    else:
        response = Response(json.dumps({"error":
                                        "Invalid Parcel delivery order object"}),
                            status=400, mimetype="application/json")
        return response


# PUT /parcels/<parcelId>/cancel
@ap.route('/api/v1/parcels/<int:id>/cancel', methods=['PUT'])
def cancel_parcel_request(id):
    '''
    cancels a specific request given its identifier
    '''
    if is_order_delivered(id):
        return jsonify({"msg": "Not allowed parcel request has already been delivered"}), 403
    for parcel in parcels:
        if parcel['id'] == id:
            cancelled_parcel = {
                'id': parcel['id'],
                'pickup_address': parcel['pickup_address'],
                'destination_address': parcel['destination_address'],
                'comment_description': parcel['comment_description'],
                'status': "cancelled",
                'current_location': parcel['current_location'],
                'created': parcel['created'],
                'user_id': parcel['user_id'],
                'recipient_address': parcel['recipient_address'],
                'recipient_phone': parcel['recipient_phone'],
                'recipient_email': parcel['recipient_email']

            }
            parcel.update(cancelled_parcel)
    if len(cancelled_parcel) == 0:
        return jsonify({"msg": "parcel request does not exist"}), 404

    return jsonify({"msg": "parcel request was cancelled successfully",
                    "status": cancelled_parcel.get("status"),
                    "id": cancelled_parcel.get("id")}), 200


def is_valid_request(newparcel):
    if "destination_address" in newparcel and "pickup_address" in newparcel \
            and "comment_description" in newparcel and "created" in newparcel and \
            "user_id" in newparcel and "recipient_address" in newparcel and "recipient_phone" in newparcel and \
            "recipient_email" in newparcel and "status" in newparcel:
        return True
    else:
        return False


def is_order_delivered(id):
    '''
    checks that we cannot cancel an already delivered order
    '''
    for parcel in parcels:
        if parcel['id'] == id:
            if parcel['status'] == 'delivered':
                return True
    return False
