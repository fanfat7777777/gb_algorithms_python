from collections import defaultdict

numb = int(input('Количество предприятий: '))

# Создание словаря
corp = defaultdict(list)
mid_sum = 0

for i in range(1, numb + 1):
    # Заполняем значение
    corp[f'Компания {i}'] = list(map(int, input(f'Доход {i} компании за кварталы(4): ').split(' ')))
    mid_sum += sum(corp[f'Компания {i}'])

# среднее значение всех компаний
mid_sum = mid_sum / numb


corp_sort = defaultdict(list)
for name, profit in corp.items():
    if sum(profit) >= mid_sum:
        corp_sort['Доход выше среднего'].append(name)
    else:
        corp_sort['Доход ниже среднего'].append(name)

print()
print(f"Доход выше среднего у: {corp_sort['Доход выше среднего']}")
print(f"Доход ниже среднего у: {corp_sort['Доход ниже среднего']}")
