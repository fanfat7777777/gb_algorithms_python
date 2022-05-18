import random

mass = [random.randint(-100, 100) for i in range(10)]
print(mass)

def function_sort(mas):
    for run in range(len(mas) - 1):
        for i in range(len(mas) - 1 - run):
            if mas[i] < mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]

function_sort(mass)
print(mass)
