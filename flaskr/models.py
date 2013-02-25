# coding: utf-8
from flaskr import db
from sqlalchemy import *

class Entry(db.Model):
    u"ブログエントリ"
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    text = Column(Text)

    def __repr__(self):
        return "<Entry id={} title={!r}>".format(self.id, self.title)

def init():
    db.create_all()
