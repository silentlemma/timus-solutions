import os
from sys import stdout

computers, cables = map(int, open(0, "rb", buffering=0).read().split())
# Doubling stops at the first power of two reaching min(computers, cables).
doublings = (min(computers, cables) - 1).bit_length()
available = 1 << doublings
print(doublings + max(0, (computers - available + cables - 1) // cables))

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
