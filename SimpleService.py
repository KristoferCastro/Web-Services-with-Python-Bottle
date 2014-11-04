from bottle import route, run, template

# the route() decorator links a URL path to a callback function
# In Rails, you have the routes.rb where you specify 
@route ('/hello/<name>') # note there contains a wild card contained in angle brackets <>
def index(name):
  return template('<b>Hello {{name}} </b>!', name= name)

run (host='localhost', port=8080)
