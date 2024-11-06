from connection import connect

def create_users_table():
    try:
        conn = connect()
        cursor = conn.cursor()
        
        sql = ''' 
        CREATE TABLE IF NOT EXISTS USERS (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(100) NOT NULL,
            user_surname VARCHAR(100) NOT NULL,
            user_age INT NOT NULL,
            user_email VARCHAR(255) NOT NULL
        )
        '''
        
        cursor.execute(sql)
        conn.commit()  
        
        print("Tabla USERS creada correctamente.")
        
    except Exception as e:
        print("Error al crear la tabla:", e)
    
    finally:
        cursor.close()  
        conn.close()   

if __name__ == "__main__":
    create_users_table()
