"""Generate a full-domain sequence length; large outputs remain generated."""

import sys

MIN_LENGTH = 2
MAX_LENGTH = 100000

n = int(sys.argv[1])
assert MIN_LENGTH <= n <= MAX_LENGTH
print(n)
