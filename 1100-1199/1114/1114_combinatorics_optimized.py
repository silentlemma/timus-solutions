from sys import stdin, stdout

boxes, red, blue = map(int, stdin.read().split())
answer = 1
for balls in (red, blue):
    # The coefficient fits 32 bits; only the final product needs a larger int.
    coefficient = 1
    for count in range(1, balls + 1):
        coefficient = coefficient * (boxes + count) // count
    answer *= coefficient
stdout.write(str(answer))
