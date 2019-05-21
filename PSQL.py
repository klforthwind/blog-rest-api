from login import *
import psycopg2


hostname = 'localhost'
#username = 'username'
#password = 'password'
database = 'forthwind'

def query( conn ) :
    cur = conn.cursor()
    cur.execute( "SELECT * FROM website.test" )
    for i,j in cur.fetchall():
        print(i,j)

def getData(name) :
    conn = psycopg2.connect( host=hostname, user=username, password=password, database=database )
    query( conn )
    conn.close()

    return "<html><p>This Works :)</p></html>"