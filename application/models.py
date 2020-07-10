#!/usr/bin/python
from application import db


# create class user for database.
class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=30)


# create class user for database.
class Course(db.Document):
    course_id = db.IntField(max_length=10, unique=True)
    title = db.StringField(max_length=100)
    description = db.StringField(max_length=255)
    credits = db.IntField()
    term = db.StringField(max_length=25)


# create class user for database.
class Enrollment(db.Document):
    user_id = db.IntField()
    course_id = db.StringField(max_length=10)
