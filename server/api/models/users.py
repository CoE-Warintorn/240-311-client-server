import mongoengine as me
import datetime

class User(me.Document):
    email = me.StringField(required=True, unique=True)
    password = me.StringField(required=True)
    created_time = me.DateTimeField(required=True,
                                    default=datetime.datetime.utcnow)
    updated_time = me.DateTimeField(required=True,
                                    default=datetime.datetime.utcnow)
    
    meta = {'collection': 'users'}