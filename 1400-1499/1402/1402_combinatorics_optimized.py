import os
import sys

count = int(sys.stdin.buffer.read())
ways, total = count, 0
for length in range(2, count + 1):
    ways *= count - length + 1
    total += ways
print(total)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
