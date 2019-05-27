from flask import Flask
from flask_restful import Api, Resource, reqparse
from database import *
import markdown2
import re

app = Flask(__name__)
api = Api(app)

# Blog REST API
class Blog(Resource):

    #GET Request- Returns website in full html
    def get(self, name):
        for post in posts :
            if (post["url"]==name) and re.match("^[A-Za-z0-9_-]*$", name):

                #Get Post HTML
                fileLoc = "posts/" + str(name) + ".md"
                data = open(fileLoc, "r")
                backToHome = "<a href=\"/blog/\"><ul><--Back To Blog</ul></a><br>"
                content = backToHome + markdown2.markdown(data.read())

                #Return the whole page in HTML
                return str(content), 200, {'Access-Control-Allow-Origin': '*'}

        return "RAWR XD", 404, {'Access-Control-Allow-Origin': '*'}
        
    #def post(self, name):
    #def put(self, name):
    #def delete(self, name):

class BlogList(Resource):
    
    #Get Request- Returns lsit of posts in full HTML
    def get(self):
        content = ""
        for post in posts:
            content += '<a href=\"?page={}\"><ul>{}<aside>{}</aside></ul></a>'.format(post["url"], post["title"], post["date"])
        #Return the whole page in HTML
        return content, 200, {'Access-Control-Allow-Origin': '*'}

# Access the api from 198.58.107.98:6969/blog/url-name
api.add_resource(Blog, "/blog/<string:name>")

# Access the api from 198.58.107.98:6969/blog/
api.add_resource(BlogList, "/blog/")

app.run(host='198.58.107.98', port=4242, debug=True, ssl_context=('/etc/letsencrypt/live/www.klforthwind.com/fullchain.pem', '/etc/letsencrypt/live/www.klforthwind.com/privkey.pem'))