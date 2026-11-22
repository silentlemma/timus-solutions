from sys import stdin

numbers = list(map(int, stdin.buffer.read().split()))
count = numbers[0]
# The header contributes count to the list sum. Cancel it without copying the list.
total = sum(numbers, -count)
print(f"{total / count:.6f}")
