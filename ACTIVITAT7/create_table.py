from connection import connect

def create_users_table():
    conn = connect()
    cursor = conn.cursor()
    
    sql = '''
    CREATE TABLE IF NOT EXISTS USERS (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        surname VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        email VARCHAR(255) NOT NULL
    )
    '''
    
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla USERS creada correctamente.")

if __name__ == "__main__":
    create_users_table()
