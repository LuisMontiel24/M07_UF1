from connection import connect

def delete_user(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USERS WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Usuario eliminado con éxito.")

if __name__ == "__main__":
    delete_user(1)