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
    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["irc_database"]
        self.user_column = self.db["users"]
        self.user_column.create_index("user_id", unique = True)
        self.user_column.create_index("username", unique = True)
        self.user_column.create_index("user_secret", unique = True)
        self.user_column.create_index("phone_number", unique = True)

    def get_user_by_username(self, username: str):
        user = self.user_column.find_one({ "username": username })
        return user

    def get_user(self, query: dict):
        user = self.user_column.find_one(query)
        return user
    
    def insert_user(self, user: User):
        self.db["users"].insert_one(user.__dict__)

