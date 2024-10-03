# exercici9.py

paraules = input("Introdueix entre 1 i 3 paraules: ").split()

if len(paraules) < 1 or len(paraules) > 3:
    print("Número de paraules no vàlid.")
else:
    for paraula in paraules:
        print(f"Paraula: {paraula}, Caràcters: {len(paraula)}, Primer caràcter: {paraula[0]}, Últim caràcter: {paraula[-1]}")
