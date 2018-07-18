import os
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                                user=username,
                                password='',
                                db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE Name = %s;",
                        rows)
        connection.commit()
        
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()