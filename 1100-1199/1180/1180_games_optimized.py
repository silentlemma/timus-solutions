import os
import sys

MODULUS = 3
digits = sys.stdin.buffer.read().strip()
# ASCII zero is divisible by three, so byte sums have the same remainder.
remainder = sum(digits) % MODULUS
print("2" if remainder == 0 else "1\n%d" % remainder)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
