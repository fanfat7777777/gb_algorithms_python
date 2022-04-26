import timeit
# Задача по сложению двух чисел
# Если я правильно понял, то сложность O(n)

print(timeit.timeit("""
numbers = ['0', '0']
sum_numb = 0
for i in range(len(numbers)):    sum_numb += float(numbers[i])"""))
# 0.7548555

print(timeit.timeit("""
numbers = ['10000', '9543548']
sum_numb = 0
for i in range(len(numbers)):    sum_numb += float(numbers[i])"""))
# 0.8600969

print(timeit.timeit("""
numbers = ['999999999999', '999999999999999']
sum_numb = 0
for i in range(len(numbers)):    sum_numb += float(numbers[i])"""))
# 0.8760481
