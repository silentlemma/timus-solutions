"""One test from a seed: a random N from 1 to 1000000."""

import random
import sys

LARGEST = 10**6

print(random.Random(int(sys.argv[1])).randint(1, LARGEST))
