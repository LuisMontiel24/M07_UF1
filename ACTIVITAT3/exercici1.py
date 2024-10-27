num = int(input("Introduce un número entre 10 y 100: "))
while num < 10 or num > 100:
    num = int(input("Número fuera de rango. Introdúcelo entre 10 y 100: "))
tupla_numeros = tuple(range(1, num + 1))
print(tupla_numeros)
