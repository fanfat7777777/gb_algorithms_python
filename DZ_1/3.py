# точка А
x1 = int(input('Введите значение x1: '))
y1 = int(input('Введите значение y1: '))

# точка B
x2 = int(input('Введите значение x2: '))
y2 = int(input('Введите значение y2: '))

# y = k * x + b
# находим k и b
k = (y2 - y1) / (x2 - x1)
b = y2 - k * x2

print(f'y = {k}x + {b}')