numbers = input('Введите последовательность чисел: ')
search_numb = input('Введите искомую цифру: ')
count = 0

for i in range(len(numbers)):
    if search_numb == numbers[i]:
        count += 1
print(f'Совпадений: {count}')
