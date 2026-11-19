import os
import sys

first, second = map(int, sys.stdin.buffer.read().split())
if first > 0 and second > 0 and (first + second) & 1:
    first, second = second, first
print(first, second)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
