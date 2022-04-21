import random

array_numb = []
for i in range(15):
    array_numb.append(random.randint(1, 100))
print(array_numb)

min_number = [0, array_numb[0], 2, array_numb[1]]

for i in range(len(array_numb)):
    if min_number[1] > array_numb[i]:
        min_number[0] = i
        min_number[1] = array_numb[i]

    if min_number[3] > array_numb[i] and i != min_number[0]:
        min_number[2] = i
        min_number[3] = array_numb[i]
print(min_number[1], min_number[3])
