areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Segon element:", areas_pis[1])
print("Últim element:", areas_pis[-1])
print("Àrea de la terrassa:", areas_pis[7])
print("Primer al tercer element:", areas_pis[:3])
print("Tercer element a l'últim:", areas_pis[2:])
print("Total àrea habitacions:", areas_pis[5] + areas_pis[11])

# Modificar àrea del lavabo y añadir patio
areas_pis[9] = 8.5
print("Nueva lista con modificación del lavabo:", areas_pis)
areas_pis.extend(["Pati Interior", 2.78])
print("Lista con 'Pati Interior' agregado:", areas_pis)
total_area = sum(area for area in areas_pis if isinstance(area, (int, float)))
print("Total àrea del pis:", total_area)
