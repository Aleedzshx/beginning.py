

students = {}
amount = int(input("\n¿Cuántos estudiantes quieres registrar? > "))

for i in range(amount):
    id = int(input(f"\nCodigo del estudiante {i + 1} > "))
    name = input(f"\nNombre del estudiante {i + 1} > ")
    students[id] = name

print("Listado de estudiantes")
for i in students:
    print(f"\n{i} -> {students[i]}")












