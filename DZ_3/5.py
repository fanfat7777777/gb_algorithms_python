import random

array_numb = []
for i in range(10):
    array_numb.append(random.randint(-100, 0))
print(array_numb)

max_negative = [0, -100]
for i in range(len(array_numb)):
    if array_numb[i] < 0:
        if array_numb[i] > max_negative[1]:
            max_negative[0] = i
            max_negative[1] = array_numb[i]

print(f'Индекс: {max_negative[0]} \nЗначение: {max_negative[1]}')
