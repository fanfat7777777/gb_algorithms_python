import random

mass = [round(random.uniform(0, 50), 2) for i in range(10)]
print(mass)

def merge_two_list(left, right):
    c = []
    i = j = 0
    while i < len(left) and(j) < len(right):
        if left[i] < right[j]:
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1
    if i < len(left):
        c += left[i:]
    if j < len(right):
        c += right[j:]
    return c

def merge_sort(mas):
    if len(mas) == 1:
        return mas
    middle = len(mas) // 2
    left = merge_sort(mas[:middle])
    right = merge_sort(mas[middle:])
    return merge_two_list(left, right)

print(merge_sort(mass))
