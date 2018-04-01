import pymysql

def connect():
    """Connect to the database. Returns connection object."""
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='password',
                                 db='wholesome',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def get_entries(connection):
    """Return all database entries"""
    with connection.cursor() as cursor:

        query = "SELECT * FROM messages"

        cursor.execute(query)

        data = cursor.fetchall()

        return data # dict

def add_message(message: str, connection):
    """Add a message from a form"""
    with connection.cursor() as cursor:
        command = ("INSERT INTO messages "
                   "VALUES (%s)")

        cursor.execute(command, message)
        connection.commit()
