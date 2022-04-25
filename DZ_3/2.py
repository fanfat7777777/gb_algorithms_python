arr_first = [8, 3, 15, 6, 4, 2]
arr_two = []

for i in range(len(arr_first)):
    if arr_first[i] % 2 == 0:
        arr_two.append(i)

print(arr_two)
