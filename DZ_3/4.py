arr = [1, 2, 5, 4, 1, 5, 6, 1, 2, 4, 6]
numb_count = [0, 0]

for i in range(len(arr)):
    count = 0
    for k in range(len(arr)):
        if arr[i] == arr[k]:
            count += 1
    if count > numb_count[0]:
        numb_count[0], numb_count[1] = count, arr[i]

print(numb_count)
