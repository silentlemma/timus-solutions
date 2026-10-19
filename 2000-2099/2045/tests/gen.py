"""Generate one full-domain size; long answers are built in the ignored test directory."""

import sys

MAX_LENGTH = 2000

n = int(sys.argv[1])
assert 1 <= n <= MAX_LENGTH
print(n)
