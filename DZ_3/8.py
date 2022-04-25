print('Вводите по 4 целые цифры через пробел')
matr = [
    list(map(int, input().split(' '))),
    list(map(int, input().split(' '))),
    list(map(int, input().split(' '))),
    list(map(int, input().split(' ')))
]


for i in range(len(matr)):
    sum_number = 0

    for k in range(len(matr[i])):
        sum_number += matr[i][k]

    matr[i].append(sum_number)


for i in range(len(matr)):
    print(matr[i])
