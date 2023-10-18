#!/usr/bin/python3
import requests
import json
import mongo_repository

credentials_file = open("account_details.json")
credentials = json.load(credentials_file)

users_file = open("users.json")
users_file = json.load(users_file)

response = requests.post(
        'https://api.46elks.com/a1/sms',
        auth = (credentials["user_id"], credentials["user_secret"]),
        data = {
            'from': 'server',
            'to': users_file["nikole"]["number"],
            'message': 'you have a message!'
            }
        )
