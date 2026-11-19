import os
import sys

first, second = map(int, sys.stdin.buffer.read().split())
print(" ".join(map(str, range(1, first + 1))))
print(" ".join(str(index * first + 1) for index in range(1, second + 1)))

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
