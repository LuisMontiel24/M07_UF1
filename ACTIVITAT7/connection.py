import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="luis",
    password="123",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()
print(cursor)

cursor.close()
conn.close()

