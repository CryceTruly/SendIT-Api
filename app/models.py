class Parcel():

    def __init__(self, id, pickup_address, destination_address,
                 comment_description, status, current_location,
                 created,
                 user_id, recipient_address, recipient_phone,
                 recipient_email):
        self.id = id
        self.pickup_address = pickup_address,
        self.destination_address = destination_address,
        self.comment_description = comment_description,
        self.status = status,
        self.current_location = current_location,
        self.created = created,
        self.user_id = user_id,
        self.recipient_address = recipient_address,
        self.recipient_phone = recipient_phone,
        self.recipient_email = recipient_email

    def __str__(self):
        return "id:{} pickup_address:{} destination_address:{}  ".format(
            self.id, self.pickup_address, self.destination_address)

    def __repr__(self):
        return "id:{} pickup_address:{} destination_address:{}  ".format(
            self.id, self.pickup_address, self.destination_address)


parcel = Parcel(1, 'startadd', 'endadd', 'myc comment', 'delivered', 'dest address', 'now', 1, 'recipt add',
                '075633333333', 'testuser@gmail.com')
print(parcel)
