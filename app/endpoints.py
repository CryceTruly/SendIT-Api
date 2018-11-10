from flask import Flask, jsonify, request, Response, json, Blueprint

import datetime
ap = Blueprint('endpoint', __name__)

# GET parcels
@ap.route('/api/v1/parcels')
def get_parcels():
    return jsonify({'parcels': parcels}), 200


# GET parcels/id
@ap.route('/api/v1/parcels/<int:id>')
def get_a_parcel(id):
    theparcel = []
    for parcel in parcels:
        if parcel['id'] == id:
            theparcel.append(parcel)
    if len(theparcel) == 0:
        return jsonify({"msg": "parcel request not found"}), 404
    return jsonify(theparcel[0]),200


# POST /parcels
@ap.route('/api/v1/parcels', methods=['POST'])
def add_parcel():
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
            'msg': "Parcel delivery successfully created",'request_id':parcel.get('id')}),
            status=201, mimetype="application/json")
        response.headers['Location'] = "parcels/" + str(parcel['id'])
        return  response
    else:
        bad_object = {
            "error": "Invalid Parcel delivery order object"
        }
        response = Response(json.dumps(bad_object),
                            status=400, mimetype="application/json")
        return response


# PUT PUT /parcels/<parcelId>/cancel
# CANCELS A SPECIFIC RESOURCE BASING ON THE PROVIDED IDENTIFIER
@ap.route('/api/v1/parcels/<int:id>/cancel', methods=['PUT'])
def cancel_parcel_request(id):
    cancelled_parcel = {}
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
        return jsonify({"msg": "parcel request was dooes not exist"}), 404

    return jsonify({"msg": "parcel request was cancelled successfully", "status": cancelled_parcel.get("status"),
                    "id": cancelled_parcel.get("id")}), 200


def is_valid_request(newparcel):
    if "destination_address" in newparcel and "pickup_address" in newparcel\
            and "comment_description" in newparcel and "created" in newparcel and \
            "user_id" in newparcel and "recipient_address" in newparcel and "recipient_phone" in newparcel and \
             "recipient_email" in newparcel and "status" in newparcel:
        return True
    else:
        return False


def user_should_cancel(item,user_id):
    #TODO a user that created the request should be the only one that can cancel it
    #TODO check if the item status is not delivered
    for p in parcels:
        if p['user_id']==user_id:
            return True
    return False


parcels =[]
