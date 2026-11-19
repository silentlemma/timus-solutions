import os
import sys

length, radix = map(int, sys.stdin.buffer.read().split())
# Two end-digit states replace binomial coefficients and repeated powers.
zero, other = 0, radix - 1
for _ in range(1, length):
    zero, other = other, (zero + other) * (radix - 1)
print(zero + other)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
