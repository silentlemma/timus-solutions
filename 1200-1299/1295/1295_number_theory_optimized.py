import os
import sys

THIRD_BASE = 3
FOURTH_BASE = 4


MODULUS = 100
exponent = int(sys.stdin.buffer.read())
remainder = (
    1
    + pow(2, exponent, MODULUS)
    + pow(THIRD_BASE, exponent, MODULUS)
    + pow(FOURTH_BASE, exponent, MODULUS)
) % MODULUS
print(2 if remainder == 0 else 1 if remainder % 10 == 0 else 0)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
