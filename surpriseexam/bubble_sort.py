arr = [7 , 3 , 1 , 2 , 4 ,5 ,9 , 5 , 8]
# Booble Sort

for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print("Lista ordenada:", arr)


# for k in arr:
#     print(bin(k)[2:])
