import sys

read = sys.stdin.buffer.readline
m = int(read())
ids = {}
stock = [0] * (m + 1)
for product in range(1, m + 1):
    amount, _, name = read().split()
    ids[name] = product
    stock[product] = int(amount)
n = int(read())
line = []
for _ in range(n):
    amount, _, name = read().split()
    line.append([ids.get(name, 0), int(amount), -1])
front = minutes = 0
while front < n:
    customer = line[front]
    product, wanted, seen = customer
    left = stock[product]
    minutes += 1
    if left >= wanted:
        stock[product] = left - wanted
    elif left == seen:
        stock[product] = 0
    elif left > 0:
        customer[2] = left
        if front + 1 == n:
            break
        line[front], line[front + 1] = line[front + 1], customer
        continue
    front += 1
print(minutes)
