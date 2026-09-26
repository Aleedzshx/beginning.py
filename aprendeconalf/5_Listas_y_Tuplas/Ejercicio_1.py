subjects = []

amount_subjects = int(input("Cuantas materias desea ingresar? :"))

for i in range(amount_subjects):
    subject = input("Ingresa la materia: ")
    subjects.append(subject)

print(f"Yo estudio estas asignaturas > {subjects}")

