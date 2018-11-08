from flask import Flask, jsonify, request, Response, json
import datetime

app = Flask(__name__)


# GET parcels
@app.route('/parcels')
def get_parcels():
    return jsonify({'parcels': parcels}), 200


# GET parcels/id
@app.route('/parcels/<int:id>')
def get_a_parcel(id):
    parcel = {}
    for parcel in parcels:
        if parcel['id'] == id:
            parcel = {
                'id': id,
                'pickup_address': parcel['pickup_address'],
                'destination_address': parcel['destination_address'],
                'comment_description': parcel['comment_description'],
                'status': parcel['status'],
                'current_location': parcel['current_location'],
                'created': parcel['created'],
                'user_id': parcel['user_id'],
                'recipient_address': parcel['recipient_address'],
                'recipient_phone': parcel['recipient_phone'],
                'recipient_email': parcel['recipient_email']

            }
            return jsonify(parcel), 200

    return jsonify(parcel)


# POST /parcels
@app.route('/parcels', methods=['POST'])
def add_parcel():
    request_data = request.get_json()
    if (is_valid_request(request_data)):
        parcel = {
            'id': len(parcels)+1,
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
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "parcels/" + str(request_data['id'])
        return jsonify({"msg": "parcel delivery requests created"}, parcel)
    else:
        bad_object = {
            "error": "Invalid Parcel delivery order object"
        }
        response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
        return response


# PUT PUT /parcels/<parcelId>/cancel
# CANCELS A SPECIFIC RESOURCE BASING ON THE PROVIDED IDENTIFIER
@app.route('/parcels/<int:id>/cancel', methods=['PUT'])
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

    return jsonify({"msg": "parcel request cancelled"}, cancelled_parcel)


def is_valid_request(newparcel):
    if "destination_address" in newparcel and "id" in newparcel and "pickup_address" in newparcel and "comment_description" in newparcel and "created" in newparcel and \
            "user_id" in newparcel and "recipient_address" in newparcel and "recipient_phone" in newparcel and "recipient_email" in newparcel and "status" in newparcel:
        return True
    else:
        return False


parcels = [
    {
        'id': 1,
        'pickup_address': 'Kampala Kikoni Makerere 13',
        'destination_address': 'Mabarara Kikoni Home 13',
        'comment_description': 'My parcels contain a laptop,please deliver',
        'status': 'In Transit',
        'current_location': 'Mabarara Kikoni Home 13',
        'created': datetime.datetime.now(),
        'user_id': 1,
        'recipient_address': 'Julie Muli',
        'recipient_phone': '0767876666',
        'recipient_email': 'recipient@email.com'

    },
    {
        'id': 2,
        'pickup_address': 'Kampala Kikoni Makerere 13',
        'destination_address': 'Mabarara Kikoni Home 13',
        'comment_description': 'My parcels contain a laptop,please deliver',
        'status': 'In Transit',
        'current_location': 'Mabarara Kikoni Home 13',
        'created': datetime.datetime.now(),
        'user_id': 33,
        'recipient_address': 'Julie Muli',
        'recipient_phone': '0767876666',
        'recipient_email': 'recipient@email.com'
    }
]

app.run(port=5000, debug=True)
