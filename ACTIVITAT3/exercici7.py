contactos = {}
while True:
    nombre = input("Introduce un nombre (o 'no' para salir): ")
    if nombre.lower() == "no":
        break
    if nombre in contactos:
        print("Este nombre ya existe en el diccionario.")
        continue
    edad = int(input("Introduce la edad: "))
    contactos[nombre] = edad
print("Diccionario de contactos:", contactos)
