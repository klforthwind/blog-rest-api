#REST Api Using Python Flask
##05/29/2019

![Python Flask](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/220px-Flask_logo.svg.png "A python web framework")

Flask is known for being a small Python web framework, not having a database abstraction layer, form validation, or anything else that is already provided by another third-party library. 

Setting up flask in a python rest api is pretty simple, since flask has a flask\_restful api that makes HTTP requests really easy. To begin, we need to import flask and flask\_restful into our python file:
```py
from flask import Flask
from flask_restful import Api, Resource, reqparse
```
You will also need to install flask and flask\_restful through the commandline:
```py
pip install flask
pip install flask_restful
```
Then we will need to add the following two lines to the code afterwards:
```py
app = Flask(__name__)
api = Api(app)
```
The declaration of app is how we will hold the Flask framework, while api will be used to handle HTTP requests, which uses the app web framework in order to access it on the website.

Then we will need to declare the resource that the rest api will be useful for. If we were to be creating a rest api that will handle Users for a certain company, we would say:
```py
class User(Resource):
```
and the rest api will most likely be handling the four HTTP requests, put, post, get and delete, which goes off of [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete "Article on CRUD). We will need to add the following functions to our new Resource class:
```py
	def get(self, name):

	def post(self, name):
    
	def put(self, name):
    
	def delete(self, name):
```

At the end of the python file, we want to add the following two lines:
```py
api.add_resource(User, "/user/<string:name>")
app.run(host=IP_ADDRESS, port=5000, debug=True)
```
The first line adds the User resource class to the flask\_restful api such that it is reachable at /user/anyUserName, which the User Resource functions will use anyUserName as the name parameter in the functions, which will actually trigger the get function if it were to be accessed from a web browser. The second line runs the flask web framework on the ip address specified on the specific port. It is important to keep in mind that it cannot run on the same port as something already running. So it will not be able to run on 443 (SSL) if you already have an https server running. If debug is on, the rest api python file will adjust if you make changes to the python file.

If the User Resource class had code for a get function, and if an array of names existed called users, this code would attempt to find said name, and try to return the name and 200 (HTTP Status Successful) or try to return "User not found" and 404 (HTTP Status Not Found):
```py
def get(self, name):
        for user in users:
            if(name == user):
                return user, 200
        return "User not found", 404
```

After running this file you should be able to access the rest api at IP_ADDRESS:5000/user/anyUserName. If you switch out IP\_ADDRESS with localhost, you should be able to access it at localhost:5000/user/anyUserName.

:)

[Example Code](https://github.com/klforthwind/blog-examples/blob/master/rest-flask-api/rest.py "Python Flask REST Api")

#####Sources:
######None
