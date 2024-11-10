from connection import connect

def update_user(user_id, name=None, surname=None, age=None, email=None):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE USERS SET name = %s, surname = %s, age = %s, email = %s WHERE id = %s",
        (name, surname, age, email, user_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Usuario actualizado con éxito.")

if __name__ == "__main__":
    update_user(1, "Luis", "Montiel", 26, "lmontiel23@ilg.cat")



