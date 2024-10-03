# exercici2.py

preu = float(input("Introdueix un valor en €: "))
iva = input("Introdueix el % d'IVA (4%, 10%, 21%): ")

while iva not in ['4', '10', '21']:
    iva = input("IVA incorrecte. Introdueix 4%, 10% o 21%: ")

iva = float(iva) / 100
preu_final = preu * (1 + iva)
print(f"Valor: {preu}€, IVA: {iva*100}%, Valor final: {preu_final}€")
