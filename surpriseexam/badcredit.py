#Examen..

print('\nPara aprobar tu credito necesitamos unos datos...')
income = int(input('\nIngrese sus ingresos mensuales > '))
score = int(input('\nIngrese su puntaje de credito de 0 a 1000 > '))
time = int(input('\nIngrese el tiempo que lleva con nosotros > '))

approved_condition = 0

if income >= 4000000:
    approved_condition += 1
if score >= 750:
    approved_condition += 1
if time >= 2:
    approved_condition += 1

if approved_condition == 3:
    print("El crédito es Aprobado")
elif approved_condition == 2:
    print("El crédito queda En estudio")
else:
    print("El crédito es Rechazado")