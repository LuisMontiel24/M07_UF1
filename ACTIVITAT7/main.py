import create
import read
import update
import delete

def main():
    while True:
        print("\n Menu de navegacion para la tabla USERS")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        choice = input("Selecciona una opción: ")
        
        if choice == "1":
            name = input("Nombre: ")
            surname = input("Apellido: ")
            age = int(input("Edad: "))
            email = input("Email: ")
            create.insert_user(name, surname, age, email)
        
        elif choice == "2":
            read.fetch_users()
        
        elif choice == "3":
            user_id = int(input("ID de usuario a actualizar: "))
            name = input("Nuevo nombre: ")
            surname = input("Nuevo apellido: ")
            age = int(input("Nueva edad: "))
            email = input("Nuevo email: ")
            update.update_user(user_id, name, surname, age, email)
        
        elif choice == "4":
            user_id = int(input("ID de usuario a eliminar: "))
            delete.delete_user(user_id)
        
        elif choice == "5":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
