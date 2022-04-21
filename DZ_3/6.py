import random

array_numb = []
for i in range(15):
    array_numb.append(random.randint(1, 100))
print(array_numb)


max_numb = [0, 0]
for i in range(len(array_numb)):
    if array_numb[i] > max_numb[1]:
        max_numb[0] = i
        max_numb[1] = array_numb[i]

min_numb = max_numb[:]
for i in range(len(array_numb)):
    if array_numb[i] < min_numb[1]:
        min_numb[0] = i
        min_numb[1] = array_numb[i]

print('максимальное', max_numb)
print('минимальное', min_numb)


def sum_numbs(min_number, max_number):
    print(min_number, max_number)
    sum_num = 0

    for i in range(min_number + 1, max_number):
        sum_num += array_numb[i]
    print(sum_num)


if max_numb[0] > min_numb[0]:
    if max_numb[0] - min_numb[0] == 1:
        print('Между макс и мин, нет значений')
    else:
        sum_numbs(min_numb[0], max_numb[0])
else:
    if min_numb[0] - max_numb[0] == 1:
        print('Между макс и мин, нет значений')
    else:
        sum_numbs(max_numb[0], min_numb[0])
