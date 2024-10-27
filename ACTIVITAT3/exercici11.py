divises = {"Euro": "€", "Dólar": "$", "Ien": "¥", "Lliura": "£"}
divisa = input("Introdueix una divisa: ")
simbol = divises.get(divisa.capitalize())
if simbol:
    print(f"El símbol de {divisa} és {simbol}.")
else:
    print("Divisa no disponible.")
