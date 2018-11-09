from flask import Flask, jsonify, request, Response, json
import datetime

app = Flask(__name__)

"""---------------------------PARCEL OPERATIONS-----------------------------"""


# GET parcels
@app.route('/parcels')
def get_parcels():
    return jsonify({'parcels': parcels}), 200


# GET parcels/id
@app.route('/parcels/<int:id>')
def get_a_parcel(id):
    theparcel = []
    for parcel in parcels:
        if parcel['id'] == id:
            theparcel.append(parcel)
    if len(theparcel) == 0:
        return jsonify({"msg": "parcel request not found"}), 404
    return jsonify(theparcel[0])


# POST /parcels
@app.route('/parcels', methods=['POST'])
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
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "parcels/" + str(parcel['id'])
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
    if len(cancelled_parcel) == 0:
        return jsonify({"msg": "parcel request was dooes not exist"}), 404

    return jsonify({"msg": "parcel request was cancelled successfully", "status": cancelled_parcel.get("status"),
                    "id": cancelled_parcel.get("id")}), 200


def is_valid_request(newparcel):
    if "destination_address" in newparcel and "pickup_address" in newparcel and "comment_description" in newparcel and "created" in newparcel and \
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

"""---------------------------------------END OF PARCEL OPERATIONS------------------------------------------------------------------------"""


@app.route('/users', methods=['GET'])
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


# CREATE A NEW USER
@app.route('/users', methods=['POST'])
def create_user():
    request_data = request.get_json()

    if is_valid_user_request(request_data):

        for user in users:
            if user['email'] == request_data['email']:
                return jsonify({"success": False, "msg": "Email is already taken"}), 200
            if user['username'] == request_data['username']:
                return jsonify({"success": False, "msg": "Username is already taken"}), 200

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
    else:
        return jsonify({"success": False, "msg": "Bad request"}), 400


@app.route('/users/<int:id>/parcels')
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

if __name__=="__main__":
   app.run(port=5000, debug=True)
