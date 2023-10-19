#!/usr/bin/python3
import requests
import mongo_repository

def send_sms(sender: dict, receiver: dict, message: str):
    sender_user_id = sender["user_id"]
    sender_secret = sender["user_secret"]
    sender_secret = sender.get("user_secret")
    if not sender_secret: raise Exception("Sender secret did not exist!")
    sender_username = sender["username"]
    receiver_phone_number = receiver["phone_number"]
    print(f"Sender user_id: {sender_user_id}, \nSender secret: {sender_secret}")

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

user1 = db.get_user_by_username("testing")
user2 = db.get_user_by_username("testing2")
send_sms(user2, user1, "HELLO THERE")

