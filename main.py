#!/usr/bin/python3
import requests
import mongo_repository

class Server(object):
    def __init__(self, db):
        self.db = db

    def send_sms(self, sender_username: str, target_username: str):
        sender_user_id = self.db.get_user_by_username(sender_username)["user_id"]
        sender_secret = self.db.get_user_by_username(sender_username)["user_secret"]
        print(f"Sender user_id: {sender_user_id}, \nSender secret: {sender_secret}")
        target_phone_number = self.db.get_user_by_username(target_username)["phone_number"]
        response = requests.post(
                'https://api.46elks.com/a1/sms',
                auth = (sender_user_id, sender_secret),
                data = {
                    'from': sender_username,
                    'to': target_phone_number,
                    'message': 'you have a message!'
                    }
                )
        print(response)

db = mongo_repository.Database()
server = Server(db)
server.send_sms("testing2", "testing")
