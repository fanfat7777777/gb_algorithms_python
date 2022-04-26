import timeit
import time

# Без решета Эратосфена
numb = 100000
flag = True

for i in range(2, numb):
    if (numb % i) == 0:
        flag = False
        break

if flag:
    print('Число простое')
else:
    print('Число не простое')

print(timeit.timeit("""
numb = 100000
flag = True
for i in range(2, numb):
    if (numb % i) == 0:
        flag = False
        break
"""), 'сек')


# С использованием решета Эратосфена
numb = 100000

numbs = {i for i in range(2, numb + 1)}
start = time.time()
for i in range(2, numb + 1):
    for k in range(i + i, numb + 1, i):
        numbs.discard(k)
end = time.time()
print(end - start, 'сек')
