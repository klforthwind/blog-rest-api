from flask import Flask
from flask_restful import Api, Resource, reqparse
from PSQL import getData
import markdown2

app = Flask(__name__)
api = Api(app)

class Blog(Resource):

    def get(self, name):
        html = getData(name)
        return html

    #def post(self, name):
    #def put(self, name):
    #def delete(self, name):

api.add_resource(Blog, "/blog/<string:name>")

app.run(host='198.58.107.98', port=6969, debug=True)