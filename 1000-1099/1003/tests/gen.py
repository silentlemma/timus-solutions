"""Random tests: the answers follow a hidden sequence until one lie.

Any parities of the prefixes (with prefix(0) = 0) describe some sequence, so
they are drawn lazily only for the positions that are asked about."""

import random
import sys

END_OF_INPUT = -1

seed, tests, questions, length = (int(x) for x in sys.argv[1:5])
rng = random.Random(seed)
lines = []
for _ in range(tests):
    prefix = {0: 0}
    lie = rng.randint(0, questions)
    lines += [str(length), str(questions)]
    for i in range(questions):
        left = rng.randint(1, length)
        right = rng.randint(left, length)
        for pos in (left - 1, right):
            prefix.setdefault(pos, rng.randint(0, 1))
        odd = prefix[right] ^ prefix[left - 1]
        if i >= lie:
            odd = rng.randint(0, 1)
        lines.append("%d %d %s" % (left, right, "odd" if odd else "even"))
lines.append(str(END_OF_INPUT))
print("\n".join(lines))
