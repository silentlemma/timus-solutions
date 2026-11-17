import sys

first, second = map(int, sys.stdin.buffer.read().split())
print("yes" if first % 2 == 0 or second % 2 == 1 else "no")
