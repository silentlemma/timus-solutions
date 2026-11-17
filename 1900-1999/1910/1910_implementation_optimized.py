WINDOW = 3

numbers = map(int, open(0, "rb").read().split())
n = next(numbers)
left, middle, right = next(numbers), next(numbers), next(numbers)
best, position = left + middle + right, 2
for i in range(WINDOW, n):
    left, middle, right = middle, right, next(numbers)
    total = left + middle + right
    if total > best:
        best, position = total, i
print(best, position)
