"""A chocolate label: a seed, N, the share of products with a given
percentage (in percent) and a mode. Mode 0 starts from a real
non-increasing recipe adding up to 100%, so the label is honest unless a
given value is nudged by mode 1, mode 2 picks the given values at random in
non-increasing order."""

import random
import sys

WHOLE = 10000
PERCENT = 100


def main():
    seed, n, shown, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if mode == 2:
        values = sorted((rng.randint(1, WHOLE) for _ in range(n)), reverse=True)
    else:
        # cut 100% into n positive parts and sort them
        cuts = sorted(rng.sample(range(1, WHOLE), n - 1)) if n > 1 else []
        bounds = [0] + cuts + [WHOLE]
        values = sorted((bounds[k + 1] - bounds[k] for k in range(n)), reverse=True)
    show = [rng.randrange(PERCENT) < shown for _ in range(n)]
    if mode == 1 and any(show):
        k = rng.choice([k for k in range(n) if show[k]])
        low = values[k + 1] if k + 1 < n and show[k + 1] else 1
        high = values[k - 1] if k > 0 and show[k - 1] else WHOLE
        values[k] = rng.randint(low, high)
        # keep the shown values in order
        shown_values = sorted((values[k] for k in range(n) if show[k]), reverse=True)
        it = iter(shown_values)
        values = [next(it) if show[k] else values[k] for k in range(n)]
    lines = [str(n)]
    for k in range(n):
        name = "P%d" % k
        lines.append("%s 1 %d" % (name, values[k]) if show[k] else "%s 0" % name)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
