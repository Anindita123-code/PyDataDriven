import os
import pymysql

username = os.getenv("C9_USER")

connection = pymysql.Connection(host='localhost',
                        user=username, passwd='', db='Chinook')

try:
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

