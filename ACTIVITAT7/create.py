from connection import connect

def insert_user(name, surname, age, email):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO USERS (name, surname, age, email) VALUES (%s, %s, %s, %s)",
            (name, surname, age, email)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Usuario agregado con éxito.")
    except Exception as e:
        print("Error al insertar usuario:", e)

if __name__ == "__main__":
    insert_user("Luis", "Montiel", 25, "lmontiel23@ilg.cat")