
while True:
    print('Для выхода введите 0')
    numbers = input('Введите два числа: ').split(' ')

    # Выход если ввели 0
    if len(numbers) == 1 and int(numbers[0]) == 0:
        print('Выход')
        break

    # Проверка деления на 0
    if int(numbers[1]) == 0:
        while int(numbers[1]) == 0:
            print('На ноль делить нельзя')
            numbers[1] = input('Введите второй символ ')

    # Выбор действий над числами
    action = input('Введите действие для чисел(+,-,*,/): ')

    # проверка правильности действия
    while (action != '+') and (action != '-') and (action != '*') and (action != '/'):
        print('Неверное действие для символов')
        action = input('Введите действие для чисел(+,-,*,/): ')

    # действие над символами
    if action == '+':
        print(int(numbers[0]) + int(numbers[1]))
    elif action == '-':
        print(int(numbers[0]) - int(numbers[1]))
    elif action == '*':
        print(int(numbers[0]) * int(numbers[1]))
    elif action == '/':
        print(int(numbers[0]) / int(numbers[1]))
