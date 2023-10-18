#!/usr/bin/python3
from dataclasses import dataclass
import pymongo

@dataclass
class User(object):
    username: str
    user_id: str
    user_secret: str
    phone_number: str

class Database(object):
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = client["database"]
        self.user_column = self.db["users"]

    def get_user_by_username(self, username: str):
        user = self.user_column.find_one({ "username": username })
        return user
    
    def insert_user(self, user: User):
        self.db["users"].insert_one(user.__dict__)

#bob = User(username="bob", user_id="u1234", user_secret="SECRET", phone_number="+42069")
