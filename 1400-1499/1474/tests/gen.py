"""Modes: N prints that integer, preserving the original single-argument mode.
random SEED LOW HIGH prints one seeded random N in the inclusive range.
"""

import random
import sys

if sys.argv[1] == "random":
    seed, low, high = map(int, sys.argv[2:5])
    assert 1 <= low <= high <= 499
    print(random.Random(seed).randint(low, high))
else:
    print(int(sys.argv[1]))
