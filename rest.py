from flask import Flask
from flask_restful import Api, Resource, reqparse
import markdown2
import re

app = Flask(__name__)
api = Api(app)

posts = {
    "first-post"
}

# Blog REST API
class Blog(Resource):

    #GET Request- Returns website in full html
    def get(self, name):
        for post in posts :
            if (post==name) :
                if re.match("^[A-Za-z0-9_-]*$", name):
                    #Get surrounding HTML
                    top = open("html/top.txt","r")
                    bottom = open("html/bottom.txt", "r")

                    #Get Post HTML
                    fileLoc = "posts/" + str(name) + ".md"
                    data = open(fileLoc, "r")
                    content = markdown2.markdown(data.read())

                    #Return the whole page in HTML
                    return str(top.read()) + content + str(bottom.read()), 200, {'Access-Control-Allow-Origin': '*'}

        return "RAWR XD", 404, {'Access-Control-Allow-Origin': '*'}
        
    #def post(self, name):
    #def put(self, name):
    #def delete(self, name):

class BlogList(Resource):
    
    #Get Request- Returns lsit of posts in full HTML
    def get(self):
        content = ""
        for post in posts:
            content += post

            #Return the whole page in HTML
            return content, 200, {'Access-Control-Allow-Origin': '*'}

# Access the api from 198.58.107.98:6969/blog/url-name
api.add_resource(Blog, "/blog/<string:name>")

# Access the api from 198.58.107.98:6969/blog/
api.add_resource(BlogList, "/blog/")

app.run(host='198.58.107.98', port=4242, debug=True, ssl_context=('/etc/letsencrypt/live/www.klforthwind.com/fullchain.pem', '/etc/letsencrypt/live/www.klforthwind.com/privkey.pem'))