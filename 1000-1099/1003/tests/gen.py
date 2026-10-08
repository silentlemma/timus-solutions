"""Deterministic parity tests, with these command-line modes:

SEED TESTS QUESTIONS LENGTH: legacy random queries, then possible lies.
cycle SEED QUESTIONS LENGTH: a random sparse prefix path, then a false closure.
consistent SEED TESTS QUESTIONS LENGTH: random queries, all true.

Any parities of the prefixes (with prefix(0) = 0) describe some sequence, so
they are drawn lazily only for the positions that are asked about."""

import random
import sys

END_OF_INPUT = -1

if sys.argv[1] == "cycle":
    seed, questions, length = (int(x) for x in sys.argv[2:5])
    assert 3 <= questions <= 5000 and questions - 1 <= length <= 10**9
    rng = random.Random(seed)
    positions = [0, length] + rng.sample(range(1, length), questions - 2)
    rng.shuffle(positions)
    prefix = {pos: rng.randint(0, 1) for pos in positions}
    prefix[0] = 0
    lines = [str(length), str(questions)]
    edges = list(zip(positions, positions[1:]))
    edges.append((positions[0], positions[-1]))
    for i, (a, b) in enumerate(edges):
        odd = prefix[a] ^ prefix[b] ^ int(i == questions - 1)
        lines.append("%d %d %s" % (min(a, b) + 1, max(a, b), "odd" if odd else "even"))
    lines.append(str(END_OF_INPUT))
    print("\n".join(lines))
    sys.exit(0)

if sys.argv[1] == "consistent":
    seed, tests, questions, length = (int(x) for x in sys.argv[2:6])
    assert tests >= 1 and 0 <= questions <= 5000 and 1 <= length <= 10**9
    rng = random.Random(seed)
    lines = []
    for _ in range(tests):
        prefix = {0: 0}
        lines += [str(length), str(questions)]
        for _ in range(questions):
            left = rng.randint(1, length)
            right = rng.randint(left, length)
            for pos in (left - 1, right):
                if pos not in prefix:
                    prefix[pos] = rng.randint(0, 1)
            odd = prefix[right] ^ prefix[left - 1]
            lines.append("%d %d %s" % (left, right, "odd" if odd else "even"))
    lines.append(str(END_OF_INPUT))
    print("\n".join(lines))
    sys.exit(0)

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
