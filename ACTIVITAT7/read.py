from connection import connect

def fetch_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USERS")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_users()
