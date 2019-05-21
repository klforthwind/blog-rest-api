from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Blog(Resource):

    def get(self, name):

    #def post(self, name):

    #def put(self, name):

    #def delete(self, name):

api.add_resource(Blog, "/blog/<string:name>")

app.run(host='198.58.107.98', port=6969, debug=True)