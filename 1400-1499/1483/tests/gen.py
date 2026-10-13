"""One test from a seed: N from 1 to 1000."""

import random
import sys

LARGEST = 1000

print(random.Random(int(sys.argv[1])).randint(1, LARGEST))
