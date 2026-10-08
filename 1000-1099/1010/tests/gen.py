"""Random function values; a seed, N and the range of the values."""

import random
import sys

seed, n, low, high = (int(x) for x in sys.argv[1:5])
rng = random.Random(seed)
print("\n".join([str(n)] + [str(rng.randint(low, high)) for _ in range(n)]))
