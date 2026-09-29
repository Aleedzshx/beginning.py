
students = {}
amount = int(input("\n¿Cuántos estudiantes quieres registrar? > "))

for i in range(amount):
    name = (input(f"\nPrimer nombre del {i + 1} estudiante  > "))
    grade = float(input(f"\nNotas de {name} > "))
    students[name] = grade

best_grade = 0
best_student = ""
for name , nota in students.items():
    if best_grade < nota:
        best_grade = nota
        best_student = name

print(f"El mejor estudiante fue {best_student} con una nota de {best_grade}")
