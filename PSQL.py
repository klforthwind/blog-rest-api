from login import *
import psycopg2

hostname = 'localhost'
#username = 'username'
#password = 'password'
database = 'forthwind'

def issue_command(command, get_data) :
    # Get connection extablished
    conn = psycopg2.connect( host=hostname, user=username, password=password, database=database )
    cur = conn.cursor()

    # Execute command
    cur.execute(command)
    cur.execute('SELECT * FROM website.blog')

    # Grab data from select or save repository if pushing
    data = cur.fetchall() if (get_data) else conn.commit()

    # Close connection after use
    conn.close()

    # Return data if selecting data
    if (get_data) :
        return data

def pushData(url, title, tags, sources, text, timestamp) :
    insert_string = 'INSERT INTO website.blog VALUES(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'
    t = '{\"' + '\",\"'.join(tags) + '\"}'
    s = '{\"' + '\",\"'.join(sources) + '\"}'
    issue_command(insert_string.format(url, title, t, s, text, timestamp), False)
    