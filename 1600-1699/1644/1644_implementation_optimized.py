import os
from sys import stdout

KNOWN_HUNGRY = 2
KNOWN_FULL = 10
tokens = iter(open(0, "rb", buffering=0).read().split())
count = int(next(tokens))
hungry, full = KNOWN_HUNGRY, KNOWN_FULL
for _ in range(count):
    amount, verdict = int(next(tokens)), next(tokens)
    if verdict == b"hungry":
        hungry = max(hungry, amount)
    else:
        full = min(full, amount)
print(full if full > hungry else "Inconsistent")

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
