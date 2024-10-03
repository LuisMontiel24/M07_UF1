# exercici10.py

paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

nova_paraula1 = paraula2[:2] + paraula1[2:]
nova_paraula2 = paraula1[:2] + paraula2[2:]
print(f"Nova paraula 1: {nova_paraula1}, Nova paraula 2: {nova_paraula2}")
