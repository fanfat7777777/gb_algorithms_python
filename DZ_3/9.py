import random

matr = [
    [],
    [],
    [],
    [],
    []
]


for i in range(len(matr)):
    for k in range(6):
        matr[i].append(random.randint(0, 9))
    print(matr[i])


max_min_numbers = -1
for i in range(len(matr[0])):
    min_number = 10
    for k in range(len(matr)):
        if matr[k][i] < min_number:
            min_number = matr[k][i]

    if min_number > max_min_numbers:
        max_min_numbers = min_number

print(f'Максимально число из минимальных по столбцам: {max_min_numbers}')
