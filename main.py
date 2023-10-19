#!/usr/bin/python3
import requests
import mongo_repository

def send_sms(sender: dict, receiver: dict, message: str):
    sender_user_id = sender.get("user_id")
    if not sender_user_id: raise Exception("Sender user_id did not exist!")
    sender_secret = sender.get("user_secret")
    if not sender_secret: raise Exception("Sender secret did not exist!")
    sender_username = sender.get("username")
    if not sender_username: raise Exception("Sender username did not exist!")
    receiver_phone_number = receiver.get("phone_number")
    if not receiver_phone_number: raise Exception("Receiver phone number did not exist!")

    response = requests.post(
            'https://api.46elks.com/a1/sms',
            auth = (sender_user_id, sender_secret),
            data = {
                'from': sender_username,
                'to': receiver_phone_number,
                'message': message
                }
            )
    print(response)

db = mongo_repository.Database()

server = db.get_user_by_username("server")
user1 = db.get_user_by_username("testing")

send_sms(server, user1, "HELLO THERE")

