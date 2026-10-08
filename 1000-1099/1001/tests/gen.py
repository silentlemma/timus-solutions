import random
import sys

MAX_VALUE = 10**18
SEPARATORS = [" ", "  ", "\n", " \n "]

seed, count = int(sys.argv[1]), int(sys.argv[2])
rng = random.Random(seed)
parts = []
for _ in range(count):
    parts.append(str(rng.randint(0, MAX_VALUE)))
    parts.append(rng.choice(SEPARATORS))
sys.stdout.write("".join(parts).rstrip() + "\n")
