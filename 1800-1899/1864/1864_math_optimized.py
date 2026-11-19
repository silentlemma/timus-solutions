import os
import sys

PERCENT = 100


tokens = iter(map(int, sys.stdin.buffer.read().split()))
count = next(tokens)
bought = [next(tokens) for _ in range(count)]
total = sum(bought)
credits = [max(0, value * (count + 1) - total) for value in bought]
# The same divisor serves every friend; compute it once, not n times.
overpaid = sum(credits)
print(" ".join(str(PERCENT * credit // overpaid) for credit in credits))

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
