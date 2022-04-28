from collections import defaultdict

numb = defaultdict(list)
for i in range(1, 3):
    numb[i] = list(map(str, input(f'Число {i}: ')))

summa = [int(''.join(i), 16) for i in numb.values()]
print(f'Сумма: {list(hex(sum(summa)).upper())[2:]}')

comp = [int(''.join(i), 16) for i in numb.values()]
print(f'Произведение: {list(hex(comp[0] * comp[1]).upper())[2:]}')