import random

print('Введите диапазон для случайного целого числа')
a = int(input('начальное значение диапазона '))
b = int(input('последнее значение диапазона '))
num = random.randint(a, b)
print(f'ваше число: {num}')
print()

print('Введите диапазон для вещественного числа')
a = int(input('начальное значение диапазона '))
b = int(input('последнее значение диапазона '))
num = random.uniform(a, b)
if random.randint(0, 1):
    num *= -1
print(f'вещественное число: {num}')
print()

print('Символы должны быть либо заглавными либо прописными')
a = ord(input('начальный символ '))
b = ord(input('последний символ '))
num = random.randint(a, b)
print(f'Случайный символ: {chr(num)}')



