#!/usr/bin/python3
import requests
from mongo_repository import User, Database
from bottle import request, post, run, response

def send_sms(sender: dict, receiver: dict, message: str):
    sender_user_id = sender.get("user_id")
    if not sender_user_id: raise Exception("Sender user_id did not exist!")
    sender_secret = sender.get("user_secret")
    if not sender_secret: raise Exception("Sender secret did not exist!")
    sender_username = sender.get("username")
    if not sender_username: raise Exception("Sender username did not exist!")
    receiver_phone_number = receiver.get("phone_number")
    if not receiver_phone_number: raise Exception("Receiver phone number did not exist!")
    sender_phone_number = sender.get("phone_number")
    if not sender_phone_number: raise Exception("Receiver phone number did not exist!")

    response = requests.post(
            'https://api.46elks.com/a1/sms',
            auth = (sender_user_id, sender_secret),
            data = {
                'from': sender_phone_number,
                'to': receiver_phone_number,
                'message': message
                }
            )
    print(response)

db = Database()

server = db.get_user_by_username("server") # Find server "user" in database
client_user = db.get_user_by_username("nikole") # Find client with username "nikole"

#send_sms(server, client_user, "Base Message") # Sends an SMS from server to the client

@post('/sms')
def sms():
    message = request.forms.message
    from_string = request.forms.get("from")
    print(from_string)
    sender = db.get_user_by_phone_number(from_string)
    sender_username = sender.get("username")

    response.body = f"{sender_username}: {message}"
    response.status=200
    return response

host_ip = ""
host_port = 5501
run(host=host_ip, port=5501, reloader = True, quiet=False)
