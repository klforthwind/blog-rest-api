from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Blog(Resource):

    def get(self, name):

    def post(self, name):

    def put(self, name):

    def delete(self, name):


app.run(debug=True)