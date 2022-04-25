count = 0

for i in range(2, 100):
    for k in range(2, 10):
        if i % k == 0:
            count += 1

print(count)
