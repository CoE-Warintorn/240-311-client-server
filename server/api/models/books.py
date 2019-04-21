import mongoengine as me
import datetime

class Book(me.Document):
    title = me.StringField()
    author = me.StringField()
    isRead = me.BooleanField()
    created_time = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)
    updated_time = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)

    meta = {'collection': 'books'}