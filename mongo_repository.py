#!/usr/bin/python3
from dataclasses import dataclass
import pymongo
from typing import Optional

@dataclass
class User(object):
    username: str
    user_id: Optional[str]
    user_secret: Optional[str]
    phone_number: str

class Database(object):
    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["irc_database"]
        self.user_column = self.db["users"]
        self.user_column.create_index("user_id", unique = True, sparse = True)
        self.user_column.create_index("username", unique = True)
        self.user_column.create_index("user_secret", unique = True, sparse = True)
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
        self.user_column.insert_one(user.__dict__)

    def edit_user(self, username: str, values: dict):
        new_values = { "$set": values }
        self.user_column.update_one({ "username": username }, new_values)
        return self.get_user_by_username(username)

    def delete_user(self, username: str):
        query = { "username": username }
        try:
            return self.user_column.delete_one(query)
        except Exception as error:
            print(f"Could not delete user '{username}' due to error: {error}")

