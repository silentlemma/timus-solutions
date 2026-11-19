import os
import sys

SAFE = 2
count, seat = map(int, sys.stdin.buffer.read().split())
print(max(0, max(seat - 1, count - seat) - SAFE))

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
