#!/usr/bin/python3
import requests
from mongo_repository import User, Database
from bottle import request, post, run

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

db = Database()

server = db.get_user_by_username("server") # Find server "user" in database
client_user = db.get_user_by_username("nikole") # Find client with username "nikole"

#send_sms(server, client_user, "HELLO THERE") # Sends an SMS from server to the client

@post('/sms')
def sms():
    message = request.get("message")
    recipient = request.get("to")
    sender = request.get("from")
    created = request.get("created")
    print(message, sender, recipient, created)
    send_sms(server, client_user, message)

   
run(host='0.0.0.0', port=5501, reloader = True, quiet=True)
