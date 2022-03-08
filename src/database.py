import email
from email.policy import default

from flask import request
import mongoengine as db
import datetime

class User(db.Document):
    username = db.StringField(required=True)
    email    = db.EmailField(unique=True)
    password = db.StringField(max_length=120)
    created_at = db.DateTimeField(default=datetime.datetime.now())
    updated_at = db.DateTimeField(onupdate=datetime.datetime.now())

    def to_json(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Bookmark(db.Document):
    body   = db.StringField(nullable=True)
    url    = db.URLField(nullable=True)
    # short_url = db.StringField(nullable=True)
    visits    = db.IntField(nullable=True, default=0)

    def __repr__(self) -> str:
        return 'User -> {self.username}'