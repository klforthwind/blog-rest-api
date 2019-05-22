from flask import Flask
from flask_restful import Api, Resource, reqparse
from PSQL import getData

app = Flask(__name__)
api = Api(app)

# Blog REST API
class Blog(Resource):

    #GET Request- Returns website in full html
    def get(self, url):
        return getData(url)
        
    #def post(self, url):
    #def put(self, url):
    #def delete(self, url):

# Access the api from 198.58.107.98:6969/blog/url-name
api.add_resource(Blog, "/blog/<string:name>")

app.run(host='198.58.107.98', port=6969, debug=True)