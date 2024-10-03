# exercici4.py

num1 = float(input("Introdueix el primer valor: "))
num2 = float(input("Introdueix el segon valor: "))
operacio = input("Introdueix l'operació (suma, resta, multiplicació, divisió): ")

if operacio == "suma":
    print(f"Suma: {num1 + num2}")
elif operacio == "resta":
    print(f"Resta: {num1 - num2}")
elif operacio == "multiplicació":
    print(f"Multiplicació: {num1 * num2}")
elif operacio == "divisió":
    print(f"Divisió: {num1 / num2}")
else:
    print("Operació no vàlida.")
