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
        if not user:
            raise Exception(f"User with username: {username} not found")
        return user

    def get_user_by_user_id(self, user_id: str):
        user = self.user_column.find_one({ "user_id": user_id })
        if not user:
            raise Exception(f"User with user_id: {user_id} not found")
        return user

    def get_user_by_phone_number(self, phone_number: str):
        user = self.user_column.find_one({ "phone_number": phone_number })
        if not user:
            raise Exception(f"User with phone_number: {phone_number} not found")
        return user

    def insert_user(self, user: User):
        self.db["users"].insert_one(user.__dict__)

    def edit_user(self, user_to_edit: User, new_user: User):
        pass
