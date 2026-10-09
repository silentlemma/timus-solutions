"""Two random lists, the first increasing and the second decreasing; a seed,
the two sizes, the value range and whether a pair summing to TARGET must
exist (1), must not exist (0) or is left to chance (2)."""

import random
import sys

TARGET = 10000
LOW, HIGH = -32768, 32767


def main():
    seed, n1, n2, spread, want = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    lo, hi = max(LOW, -spread), min(HIGH, spread)
    first = sorted(rng.randint(lo, hi) for _ in range(n1))
    present = set(first)
    second = []
    while len(second) < n2:
        b = rng.randint(LOW, HIGH)
        if want == 0 and TARGET - b in present:
            continue
        second.append(b)
    if want == 1:
        a = rng.choice(first)
        if LOW <= TARGET - a <= HIGH:
            second[rng.randrange(n2)] = TARGET - a
    second.sort(reverse=True)
    print("\n".join(map(str, [n1] + first + [n2] + second)))


if __name__ == "__main__":
    main()
