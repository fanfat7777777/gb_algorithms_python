a = int(input('Введите 1 число '))
b = int(input('Введите 2 число '))
c = int(input('Введите 3 число '))

print(f'{a}, {b}, {c}')
if c < a < b or b < a < c:
    print('первое число является средним')
elif a < b < c or c < b < a:
    print('второе число является средним')
elif a < c < b or b < c < a:
    print('третье число является средним')