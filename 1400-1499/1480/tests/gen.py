"""Modes:
N: print N, preserving the original single-argument mode.
random SEED LO HI: print a seeded uniformly random N in the inclusive range.
"""

import random
import sys

if sys.argv[1] == "random":
    seed, lo, hi = map(int, sys.argv[2:])
    if not 2 <= lo <= hi <= 50:
        raise ValueError("N must be in 2..50")
    sys.stdout.reconfigure(newline="\n")
    print(random.Random(seed).randint(lo, hi))
else:
    print(int(sys.argv[1]))
