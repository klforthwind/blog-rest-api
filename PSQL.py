from login import *
import psycopg2

hostname = 'localhost'
#username = 'username'
#password = 'password'
database = 'forthwind'

def issue_command(command, get_data) :
    conn = psycopg2.connect( host=hostname, user=username, password=password, database=database )
    cur = conn.cursor()
    cur.execute( command )
    if (get_data) :
        data = cur.fetchall()
    conn.close()
    if (get_data) :
        return data

def pushData(url, title, tags, sources, text, timestamp) :
    insert_string = "INSERT INTO website.blog VALUES('{}','{}','{}','{}','{}','{}')"
    t = '{\"' + '\",\"'.join(tags) + '\"}'
    s = '{\"' + '\",\"'.join(sources) + '\"};'
    issue_command(insert_string.format(url, title, t, s, text, timestamp), False)
    