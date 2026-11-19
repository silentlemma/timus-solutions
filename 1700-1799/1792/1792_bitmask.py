import os
from sys import stdout

DATA = 4
CHECKS = 3
ALL_CHECKS = (1 << CHECKS) - 1

word = list(map(int, open(0, "rb", buffering=0).read().split()))
parity = sum(word[:DATA]) & 1
syndrome = sum((parity ^ word[j] ^ word[DATA + j]) << j for j in range(CHECKS))
if syndrome:
    # A parity bit affects one check; data bits affect all but their own check.
    if syndrome & (syndrome - 1) == 0:
        position = DATA + syndrome.bit_length() - 1
    elif syndrome == ALL_CHECKS:
        position = DATA - 1
    else:
        position = (ALL_CHECKS ^ syndrome).bit_length() - 1
    word[position] ^= 1
print(*word)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
