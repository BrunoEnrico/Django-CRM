import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE DjangoCRM")