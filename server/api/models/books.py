import mongoengine as me
import datetime

class Book(me.Document):
    title = me.StringField(required=True)
    author = me.StringField(required=True)
    is_read = me.BooleanField(required=True)
    created_time = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)
    updated_time = me.DateTimeField(required=True,
                                    default=datetime.datetime.now)

    meta = {'collection': 'books'}

    def to_dict(self):
        return dict(id=str(self.id),
                    title=self.title,
                    author=self.author,
                    is_read=self.is_read)