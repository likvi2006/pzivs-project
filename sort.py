import random

arr = []
i = 0
while i < 10:
    arr.append(random.randint(1, 100))
    i += 1

print("Початковий масив:", arr)

n = len(arr)
i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if arr[j] > arr[j + 1]:
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp
        j += 1
    i += 1

print("Відсортований масив:", arr)
