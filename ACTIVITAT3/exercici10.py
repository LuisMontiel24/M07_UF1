abecedari = list("abcdefghijklmnopqrstuvwxyz")
abecedari = [lletra for i, lletra in enumerate(abecedari) if (i + 1) % 3 != 0]
tupla_abecedari = tuple(abecedari)
print("Llista de lletres:", abecedari)
print("Tupla de lletres:", tupla_abecedari)
