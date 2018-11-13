from flask import jsonify, request, Blueprint

from app.model.parcel import ParcelList

ap = Blueprint('endpoint', __name__)
PARCEL = ParcelList()


@ap.route("/")
def welcome():
    return jsonify({"message": "Welcome to the sendit api,v1"})


# GET parcels
@ap.route('/api/v1/parcels')
def get_parcels():
    '''
    returns a list of all requests
    '''
    all = PARCEL.get_all_parcel()
    if all:
        return jsonify({'count': len(all), 'orders': all}), 200
    return jsonify({'msg': 'no parcel delivery orders posted yet', 'count': len(all)}), 404


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
    if not request.data == None:
        not_validresponse()
    if not PARCEL.is_valid_request(request.get_json()):
        not_validresponse()

    return PARCEL.add_parcel(request.get_json())


# PUT /parcels/<parcelId>/cancel
@ap.route('/api/v1/parcels/<int:id>/cancel', methods=['PUT'])
def cancel_parcel_request(id):
    '''
    cancels a specific request given its identifier
    '''
    if not PARCEL.is_parcel_exist(id):
        return jsonify({"msg": "parcel delivery request not found"}), 404

    if PARCEL.is_order_delivered(id):
        return jsonify({"msg": "Not allowed parcel request has already been delivered"}), 403
    PARCEL.cancel_parcel(id)
    return jsonify(
        {"msg": "parcel request was cancelled successfully", "status": PARCEL.cancel_parcel(id).get("status"),
         "id": PARCEL.cancel_parcel(id).get("id")}), 200


def not_validresponse():
    return jsonify({"error": 'Bad Request object,expected data is missing'}), 400
