import sys

m, n = map(int, sys.stdin.buffer.read().split())
# Each break adds one piece, so there are m*n-1 moves.
print("[:=[first]" if m * n % 2 == 0 else "[second]=:]")
