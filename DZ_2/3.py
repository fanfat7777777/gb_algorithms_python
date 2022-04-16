number = input('Введите число: ')
i = len(number) - 1
sort_number = ''

while i >= 0:
    sort_number += number[:][i]
    i -= 1
print(sort_number)