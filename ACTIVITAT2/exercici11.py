# exercici11.py

import random

numero_secreta = random.randint(1, 100)
intents = 0
endevinat = False

while not endevinat:
    intent = int(input("Endevina el número entre 1 i 100: "))
    intents += 1
    if intent < numero_secreta:
        print("El número és més gran.")
    elif intent > numero_secreta:
        print("El número és més petit.")
    else:
        print(f"Has encertat! El número era {numero_secreta}. Intents: {intents}")
        endevinat = True
