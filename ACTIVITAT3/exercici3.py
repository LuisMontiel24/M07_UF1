num = int(input("Introduce un número del 1 al 10 para ver su tabla de multiplicar: "))
while num < 1 or num > 10:
    num = int(input("Número fuera de rango. Introdúcelo entre 1 y 10: "))
tabla_multiplicar = tuple(num * i for i in range(1, 11))
print("Tabla de multiplicar:", tabla_multiplicar)
