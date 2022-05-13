# Версия: Python 3.9.5
# Разрядность ОС: 64

# Ну из нижеприведённого, логично то, что чем меньше переменных, тем меньше памяти потребуется
# Задачи 2 и 7 с одинаковым количеством переменных, но в задаче 2 одна переменная хранит текст = 51 бит,
# собственно это и увеличило потребляемую память, если были бы всё цифры, потребляемый обём был бы равен

# Как я понимаю, для уменьшения потребления памяти имеет смысл ограничивать максимальный хранимый объём
# в переменной с текстом

import sys

# Домашнее задание 2, задача 2
even_number = 0         # чётное
not_even_number = 0     # не чётное

numbers = '23'
numbers.


for i in range(0, len(numbers)):
    if i % 2 == 0:
        even_number += 1
    else:
        not_even_number += 1

#print(f'Чётных чисел: {even_number}')
#print(f'Нечётных чисел: {not_even_number}')
print(f'Задача 2, выделено: '
      f'{sys.getsizeof(even_number) + sys.getsizeof(not_even_number) + sys.getsizeof(numbers) + 28} '
      f'байт на переменные(even_number, not_even_number, numbers, i)')



# Домашнее задание 2, задача 5
kod = 32

while kod <= 127:

    for i in range(10):
        kod += 1
        if kod <= 127:
            print(end=' ')
            #print(f'"{chr(kod)}"', end=' ')
        else:
            break

    #print()
print()
print(f'Задача 5, выделено: {sys.getsizeof(kod) + 28} байт на переменные(kod и i)')



# Домашнее задание 2, задача 7
n = 10
s = 0
for i in range(1,n+1):
    s += i
    # print(s, i)
m = n * (n + 1) // 2
#print(s)
#print(m)
print()
print(f'Задача 7, выделено: {sys.getsizeof(m) + sys.getsizeof(s) + sys.getsizeof(m) + 28} '
      f'байт на все переменные(n, s, m, i)')
