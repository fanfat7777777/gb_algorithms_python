num1 = int(input('Введите 3х значное целое число: '))
summa = 0
pr = 1

pr *= num1 % 10
summa += num1 % 10
num1 = num1 // 10
summa += num1 % 10 + num1 // 10
pr *= num1 % 10 * (num1 // 10)

print(summa)
print(pr)
