import os
from sys import stdout

PARITY_PERIOD = 4
BLACK_RESIDUE = 3


size = int(open(0, "rb", buffering=0).read())
# The parity of n(n+1)/2 repeats every four values of n.
print("black" if size % PARITY_PERIOD in (0, BLACK_RESIDUE) else "grimy")

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
