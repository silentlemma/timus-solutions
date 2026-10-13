"""One test from a seed: a random radius from 1 to 100000."""

import random
import sys

LARGEST = 100000

print(random.Random(int(sys.argv[1])).randint(1, LARGEST))
