import sys

number, marks = sys.stdin.buffer.read().split()
step = len(marks)
product = 1
for factor in range(int(number), 0, -step):
    product *= factor
print(product)
