meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
while True:
    num = int(input("Introduce un número entre 0 y 12 (0 para salir): "))
    if num == 0:
        break
    elif 1 <= num <= 12:
        print(f"El mes correspondiente es: {meses[num - 1]}")
    else:
        print("Número fuera de rango.")
