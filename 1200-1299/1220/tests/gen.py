"""Stack operations: a seed, N, the number of stacks used and a mode.
Mode 1 mixes pushes and pops at random, mode 2 pushes everything first
and then pops it all, mode 3 keeps a few values in every stack so that
the most blocks are partly full, mode 4 grows one stack only."""

import random
import sys

TOP = 10**9


def main():
    seed, n, stacks, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    sizes = [0] * (stacks + 1)
    ops = []
    for i in range(n):
        live = [s for s in range(1, stacks + 1) if sizes[s]]
        if mode == 2:
            pop = i >= n // 2 and live
        elif mode == 3:
            pop = i % 3 == 2 and live
        elif mode == 4:
            pop = rng.random() < 0.3 and live
        else:
            pop = rng.random() < 0.4 and live
        if pop:
            s = rng.choice(live)
            sizes[s] -= 1
            ops.append("POP %d" % s)
        else:
            s = 1 if mode == 4 else rng.randint(1, stacks)
            sizes[s] += 1
            ops.append("PUSH %d %d" % (s, rng.randint(0, TOP)))
    sys.stdout.write("\n".join([str(n)] + ops) + "\n")


if __name__ == "__main__":
    main()
