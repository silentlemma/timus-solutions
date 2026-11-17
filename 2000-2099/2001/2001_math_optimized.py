import sys

a1, b1, _, b2, a3, _ = map(int, sys.stdin.buffer.read().split())
print(a1 - a3, b1 - b2)
