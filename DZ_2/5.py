kod = 32

while kod <= 127:

    for i in range(10):
        kod += 1
        if kod <= 127:
            print(f'"{chr(kod)}"', end=' ')
        else:
            break

    print()
