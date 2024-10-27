# Versió 1 - amb llista de notes
assignatures = ["Matemàtiques", "Física", "Química", "Història", "Geografia", "Informàtica"]
notes = []
for asignatura in assignatures:
    nota = float(input(f"Indica la nota per a {asignatura}: "))
    notes.append(nota)
for asignatura, nota in zip(assignatures, notes):
    print(f"A {asignatura} ha tret {nota}.")

# Versió 2 - amb diccionari
notes_dict = {asignatura: float(input(f"Indica la nota per a {asignatura}: ")) for asignatura in assignatures}
for asignatura, nota in notes_dict.items():
    print(f"A {asignatura} ha tret {nota}.")
