
array = [5,8,5,12,8,20,15,20]
array_organized = []

for i in array:
    repetido = False
    for j in array_organized:
        if i == j:
            repetido = True
            break
    if not repetido:
        array_organized.append(i)

print(array_organized)
