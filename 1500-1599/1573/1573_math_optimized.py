import os
import sys

tokens = iter(sys.stdin.buffer.read().split())
bags = {colour: int(next(tokens)) for colour in (b"Blue", b"Red", b"Yellow")}
count = int(next(tokens))
answer = 1
for _ in range(count):
    answer *= bags[next(tokens)]
print(answer)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
