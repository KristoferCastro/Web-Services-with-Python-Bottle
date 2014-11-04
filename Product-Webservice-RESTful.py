# we will try to create a RESTful web service using Bottle.py around products
from bottle import route, run, get, post, delete, put, request, abort, response
from pymongo import MongoClient
import json
# RESTful web services is all about making use of a universal interface to perform common
# tasks like create, retrieve, update and delete.  We can do this using HTTP's VERBS.
# the alternative, non-restful, way is to use the URL to identify the operation.
# for example GET '/product/delete/17' this isn't restful!

mongodb_port = 27017

# open up a new mongo db database instance
client = MongoClient('localhost', mongodb_port)
db = client['test-products-db'] 

@post('/product')
def create_product():
  data = request.body.readline()
  if not data: # the client forgot to give us the product details
    abort(400, "No product data recieved from you") 
  
  entity = json.loads(data)
  
  product_id = db['products'].insert(entity)
  
  product_entity = db['products'].find_one({"_id":product_id})  
  response.content_type = 'application/json'
  return "Just created a product named: " + product_entity['name']

@put('/product/<id>')
def update_product(id):
  return "updated product with id: " + id

@delete('/product/<id>')
def delete_product(id):
 return "deleted product with id: " + id

@get('/product/<id>')
def retrieve_product(id):
 return "retrieve product with id: " + id

@get('/product')
def retrieve_all_products():
 products = db['proudcts'].find()
 return "There are %d products in the mongodb"%(products.count())

run(host='localhost', port=8080)
