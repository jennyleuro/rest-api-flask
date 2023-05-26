from db import db

class ItemModel(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String)
    price = db.Column(db.Float(precision = 2), unique = False, nullable = False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), unique = False, nullable = False)
    store = db.relationship('StoreModel', back_populates = 'item')
    tags = db.relationship('TagModel', back_populates = 'item', secondary = "items_tags")