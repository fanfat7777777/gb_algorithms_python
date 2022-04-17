numbers = input('Введите значения ').split(' ')
sum_numb = 0

for i in range(len(numbers)):
    sum_numb += float(numbers[i])
print(sum_numb)