import os
import sys

value = int(sys.stdin.buffer.read())
square = value * value
print(square, square + value + 1, square + 1)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
