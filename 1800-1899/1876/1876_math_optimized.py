LEGS = 40

left, right = map(int, input().split())
print(LEGS + (2 * left - 1 if left > right else 2 * right))
