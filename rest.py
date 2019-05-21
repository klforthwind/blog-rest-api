from flask import Flask
from flask_restful import Api, Resource, reqparse
import psycopg2

app = Flask(__name__)
api = Api(app)

hostname = 'localhost'
username = 'username'
password = 'password'
database = 'forthwind'

def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute( "SELECT * FROM website.test" )
    for i,j in cur.fetchall():
        print(i,j)


class Blog(Resource):

    def get(self, name):
        myConnection = psycopg2.connect( host=hostname, user=username, password=password, database=database )
        doQuery( myConnection )
        myConnection.close()
        return "<html><p>This Works :)</p></html>"

    #def post(self, name):

    #def put(self, name):

    #def delete(self, name):

api.add_resource(Blog, "/blog/<string:name>")

app.run(host='198.58.107.98', port=6969, debug=True)