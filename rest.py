from flask import Flask
from flask_restful import Api, Resource, reqparse
import markdown2
import re

app = Flask(__name__)
api = Api(app)

# Blog REST API
class Blog(Resource):

    #GET Request- Returns website in full html
    def get(self, name):
        # Hoping this stops SQL injection
        if re.match("^[A-Za-z0-9_-]*$", name):
            #Get surrounding HTML
            top = open("html/top.txt","r")
            bottom = open("html/bottom.txt", "r")

            #Get Post HTML
            fileLoc = "posts/" + str(name) + ".md"
            data = open(fileLoc, "r")
            content = markdown2.markdown(data.read())

            #Return the whole page in HTML
            return str(top.read()) + content + str(bottom.read())
        else:
            return "RAWR XD"
        
    #def post(self, name):
    #def put(self, name):
    #def delete(self, name):

# Access the api from 198.58.107.98:6969/blog/url-name
api.add_resource(Blog, "/blog/<string:name>")

app.run(host='198.58.107.98', port=6969, debug=True)