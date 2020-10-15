from flask import Flask, jsonify, request
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)

# connecting with MongoDB
cluster = pymongo.MongoClient(
    "mongodb+srv://user:1234@productsdata.oimyn.mongodb.net/eCommerce?retryWrites=true&w=majority")
db = cluster["eCommere"]
collection = db["ProductsData"]

# base route for our API
@app.route('/')
def index():
    # it just returns a welcome message so that user can check 
    # whether everything is working fine or not
    message = {
        'status': 200,
        'message': 'Welcome to eCommerce API v0.0.9'
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp

# read end point takes two path parameters
@app.route('/read/<column>/<value>', methods=['GET'])
def showProduct(column, value):
    try:
        # if user is searching with "_id" then we convert value from string to ObjectId
        if column == "_id":
            products = list(collection.find({column: ObjectId(value)}))
            
        # if user has not provided any filter then we show all data in database
        elif column == "none":
            products = list(collection.find())
        
        # we check if the value has int data as string if so then we change it to int
        elif value.isdigit():
            value = int(value)
            products = list(collection.find({column: value}))
            
        # this allows the user to search with fields which contain no value
        # like "classification_l3" = ""
        elif value == "none":
            value = ""
            products = list(collection.find({column: value}))
        
        else:
            products = list(collection.find({column: value}))

        # after getting the "products" we change "_id" from ObjectId to string
        # so that the user can use it use it easily
        for product in products:
            product["_id"] = str(product["_id"])
            
        # converting into JSON and returning the response
        resp = dumps(products)
        return resp
    
    # handles any exception that may occur due to Bad user inputs
    except Exception as ex:
        message = {
            'status': 400,
            'message': str(ex)
        }
        resp = jsonify(message)
        resp.status_code = 400
        return resp


@app.route('/create', methods=['POST'])
def addProduct():
    try:
        product = {
            'name': request.json['name'],
            'brand_name': request.json['brand_name'],
            'regular_price_value': request.json['regular_price_value'],
            'offer_price_value': request.json['offer_price_value'],
            'currency': request.json['currency'],
            'classification_l1': request.json['classification_l1'],
            'classification_l2': request.json['classification_l2'],
            'classification_l3': request.json['classification_l3'],
            'classification_l4': request.json['classification_l4'],
            'image_url': request.json['image_url']
        }

        if (product['name'] and product['regular_price_value'] and product['offer_price_value'] and product[
            'currency'] and
                product['classification_l1'] and product['classification_l2'] and product['image_url']):

            dbResponse = collection.insert_one(product)

            message = {
                'status': 201,
                'message': 'Product added successfully with ID: ' + str(dbResponse.inserted_id)
            }
            resp = jsonify(message)
            resp.status_code = 201
            return resp

        else:
            message = {
                'status': 400,
                'message': 'Could not add product. Please check your input and try again.'
            }
            resp = jsonify(message)
            resp.status_code = 400
            return resp

    except Exception as ex:
        message = {
            'status': 400,
            'message': str(ex)
        }
        resp = jsonify(message)
        resp.status_code = 400
        return resp


@app.route('/update/<id>', methods=['PUT'])
def updateProduct(id):
    try:
        dbResponse = collection.update_one(
            {"_id": ObjectId(id)},
            {"$set":
                {
                    "name": request.json["name"],
                    "brand_name": request.json["brand_name"],
                    "regular_price_value": request.json["regular_price_value"],
                    "offer_price_value": request.json["offer_price_value"],
                    "currency": request.json["currency"],
                    "classification_l1": request.json["classification_l1"],
                    "classification_l2": request.json["classification_l2"],
                    "classification_l3": request.json["classification_l3"],
                    "classification_l4": request.json["classification_l4"],
                    "image_url": request.json["image_url"]
                }
            }
        )
        if (dbResponse.modified_count == 1):
            message = {
                'status': 200,
                'message': 'Product with ID: ' + id + ' is successfully updated.'
            }
            resp = jsonify(message)
            resp.status_code = 200
            return resp

        else:
            message = {
                'status': 200,
                'message': 'Nothing to update.'
            }
            resp = jsonify(message)
            resp.status_code = 200
            return resp

    except Exception as ex:
        message = {
            'status': 404,
            'message': str(ex)
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp


@app.route('/delete/<id>', methods=['DELETE'])
def deleteProduct(id):
    try:
        dbResponse = collection.delete_one({'_id': ObjectId(id)})

        if dbResponse.deleted_count == 1:
            message = {
                'status': 200,
                'message': 'Product with ID: ' + id + ' is successfully deleted.'
            }
            resp = jsonify(message)
            resp.status_code = 200
            return resp

        else:
            message = {
                'status': 400,
                'message': 'Invalid ID: ' + str(id) + '. Please make sure ID is correct.'
            }
            resp = jsonify(message)
            resp.status_code = 400
            return resp

    except Exception as ex:
        message = {
            'status': 400,
            'message': str(ex)
        }
        resp = jsonify(message)
        resp.status_code = 400
        return resp


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
