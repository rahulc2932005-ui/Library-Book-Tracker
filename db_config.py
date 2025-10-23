import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # your MySQL username
        password="Ra_2311003020808",  # your MySQL password
        database="library_db"     # your DB name
    )

