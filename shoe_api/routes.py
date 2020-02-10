# import for shoe_api
from shoe_api import app,db
from shoe_api.models import product_schema,products_schema,Product

# Flask imports for gathering and displaying data
from flask import request,jsonify

# CORS Import
from flask_cors import CORS

CORS(app)

# CREATE PRODUCT ENDPOINT (AKA CREATE PRODUCT ROUTE)
@app.route('/product', methods = ['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    photo = request.json['photo']
    color_way = request.json['color_way']

    new_product = Product(name,description,price,qty,photo,color_way)

    # SEND DATA TO DATABASE
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# GET A SINGLE PRODUCT
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# GET MULTIPLE PRODUCTS
@app.route('/product', methods=["GET"])
def get_all_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# UPDATE A PRODUCT
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    # Get the product that we want to update based on its id
    product = Product.query.get(id)

    # Tell endpoint what to update
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    photo = request.json['photo']
    color_way = request.json['color_way']

    # Save the updated value to database
    product.name = name
    product.description = description
    product.price = price
    product.qty = qty
    product.photo = photo
    product.color_way = color_way

    # Commit the changes of values into Database
    db.session.commit()

    return product_schema.jsonify(product)


# DELETE PRODUCT
@app.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
    # Look for a product to delete by its id
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)