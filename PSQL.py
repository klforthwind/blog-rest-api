import psycopg2

hostname = 'localhost'
username = 'username'
password = 'password'
database = 'forthwind'

def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute( "SELECT * FROM website.test" )
    for i,j in cur.fetchall():
        print(i,j)

def getData(name) :
    myConnection = psycopg2.connect( host=hostname, user=username, password=password, database=database )
    doQuery( myConnection )
    myConnection.close()

    return "<html><p>This Works :)</p></html>"