import psycopg2

def connect():
    conn = psycopg2.connect(
        database="postgres",
        user="luis",
        password="123",
        host="localhost",
        port="5432"
    )
    return conn
