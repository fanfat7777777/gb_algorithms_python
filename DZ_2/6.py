import random

number = random.randint(0, 101)

otvet = False
print('Угадай число')
for i in range(10):
    guess = int(input(f'Попытка {i + 1}(макс попыток 10): '))
    if guess == number:
        print('Ты угадал')
        otvet = True
        break
    elif guess > number:
        print('Загаданное число меньше')
    elif guess < number:
        print('Загаданное число больше')
    if otvet == False and i == 9:
        print()
        print('Попытки закончились')
        print(f'Загаданное число: {number}')
