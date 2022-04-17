even_number = 0         # чётное
not_even_number = 0     # не чётное

numbers = input('Введите число ')


for i in range(0, len(numbers)):
    if i % 2 == 0:
        even_number += 1
    else:
        not_even_number += 1

print(f'Чётных чисел: {even_number}')
print(f'Нечётных чисел: {not_even_number}')