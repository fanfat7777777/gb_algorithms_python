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

array_numb[max_numb[0]] = min_numb[1]
array_numb[min_numb[0]] = max_numb[1]

print(array_numb)
print('максимальное', max_numb)
print('минимальное', min_numb)
