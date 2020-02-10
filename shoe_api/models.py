# Import of app and db
from shoe_api import app,db

# Import flask-marshmallow
from flask_marshmallow import Marshmallow

# Instantiate Marshmallow
ma = Marshmallow(app)

class Product(db.Model):
    # id, name, description, price, qty, photo, color_way
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = True)
    description = db.Column(db.String(250))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    photo = db.Column(db.String(250))
    color_way = db.Column(db.String(100))

    def __init__(self,name,description,price,qty,photo,color_way):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
        self.photo = photo
        self.color_way = color_way

# Create class using Marshmallow to create a ProductSchema
# A Schema is a demo of how our JSON data will look when created

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price','qty','photo','color_way')

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)