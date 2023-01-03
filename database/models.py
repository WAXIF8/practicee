from .db import  db

class Login(db.Document):
    name=db.StringField(required=True)
    email=db.StringField(required=True)
    password=db.StringField(required=True)

class contects(db.Document):
    name=db.StringField(required=True)
    mobile=db.StringField(required=True)

class Patients(db.Document):
    name=db.StringField(required=True)
    age=db.StringField(required=True)
    bloodGroup=db.StringField(required=True)
    contact=db.StringField(required=True)
    doctorid=db.StringField(required=True)


class Doctor(db.Document):
    name=db.StringField(required=True)
    age=db.StringField(required=True)
    contact=db.StringField(required=True)
    spec=db.StringField(required=True)
