frase = input("Introduce una frase: ").replace(" ", "")
tupla_frase = tuple(frase)
sin_repeticiones = "".join(sorted(set(frase), key=frase.index))
print("Tupla sin espacios:", tupla_frase)
print("Frase sin caracteres repetidos:", sin_repeticiones)