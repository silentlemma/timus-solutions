"""An empire whose missing channels form one Euler circuit through A: a
seed, N, the number of missing channels wanted (at most) and the longest
loop. Missing channels are laid as edge-disjoint directed loops, each one
starting at a planet that earlier loops already reach, so every planet is
balanced and all of them hang together with A."""

import random
import sys


def main():
    seed, n, want, longest = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    a = rng.randint(1, n)
    missing = set()
    touched = [a]
    tries = 0
    while len(missing) < want and tries < 50 * want:
        tries += 1
        size = rng.randint(2, min(longest, n))
        loop = [rng.choice(touched)] + rng.sample(range(1, n + 1), size - 1)
        if len(set(loop)) != size:
            continue
        edges = [(loop[k], loop[(k + 1) % size]) for k in range(size)]
        if len(missing) + size > want or any(e in missing for e in edges):
            continue
        missing.update(edges)
        touched += loop[1:]
    lines = ["%d %d" % (n, a)]
    for i in range(1, n + 1):
        lines.append(" ".join("0" if i == j or (i, j) in missing else "1" for j in range(1, n + 1)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
