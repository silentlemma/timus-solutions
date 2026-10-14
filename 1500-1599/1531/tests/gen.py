"""One test from a seed: a random n from 1 to 2000."""

import random
import sys

LARGEST = 2000

print(random.Random(int(sys.argv[1])).randint(1, LARGEST))
