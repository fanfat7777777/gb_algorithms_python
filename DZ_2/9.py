natural_numb = input('Введите натуральные числа: ').split()
max_numb = [0, 0]   # Число, сумма

for i in range(len(natural_numb)):
    sum_numb = 0
    if len(natural_numb[i]) > 1:
        for k in range(len(natural_numb[i])):
            sum_numb += int(natural_numb[i][k])
    elif int(natural_numb[i]) > max_numb[1]:
        max_numb[0] = max_numb[1] = int(natural_numb[i])

    if sum_numb > max_numb[1]:
        max_numb[0] = int(natural_numb[i])
        max_numb[1] = sum_numb

print(f'Число: {max_numb[0]} Сумма его цифр: {max_numb[1]}')
