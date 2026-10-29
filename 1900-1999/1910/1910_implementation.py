import sys

data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1 : n + 1]))
# try every section as the middle of the three
best, middle = 0, 0
for i in range(1, n - 1):
    total = a[i - 1] + a[i] + a[i + 1]
    if total > best:
        best, middle = total, i
print(best, middle + 1)
