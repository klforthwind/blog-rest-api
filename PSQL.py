from login import *
import psycopg2

hostname = 'localhost'
#username = 'username'
#password = 'password'
database = 'forthwind'

def getData(name) :
    conn = psycopg2.connect( host=hostname, user=username, password=password, database=database )
    cur = conn.cursor()
    cur.execute( "SELECT * FROM website.test" )
    data = cur.fetchall()
    conn.close()
    
    return data