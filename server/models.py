
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# Configure metadata for foreign key naming convention
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)



class Bakery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    baked_goods = db.relationship('BakedGood', backref='bakery')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def to_dict_with_baked_goods(self):
        return {
            'id': self.id,
            'name': self.name,
            'baked_goods': [baked_good.to_dict() for baked_good in self.baked_goods]
        }


class BakedGood(db.Model):
    __tablename__ = 'baked_goods'

    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'bakery_id': self.bakery_id
        }

