"""Stack operations: a seed, N, the number of stacks used and a mode.
Mode 1 mixes pushes and pops at random, mode 2 pushes everything first
and then pops it all, mode 3 keeps a few values in every stack so that
the most blocks are partly full, mode 4 grows one stack only.
Mode 5 repeatedly empties random stacks, mode 6 fills the last stack
before a single pop, and mode 7 randomly recycles top blocks above
full older blocks, then drains every stack (N >= 40 * stacks)."""

import random
import sys

TOP = 10**9


def main():
    seed, n, stacks, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    sizes = [0] * (stacks + 1)
    ops = []
    if mode == 5:
        for i in range(n // 2):
            s = rng.randint(1, stacks)
            v = (0, TOP, rng.randint(0, TOP))[i % 3]
            ops.extend(["PUSH %d %d" % (s, v), "POP %d" % s])
        if n % 2:
            ops.append("PUSH %d 0" % stacks)
    elif mode == 6:
        assert n >= 2
        ops = ["PUSH %d %d" % (stacks, rng.randint(0, TOP)) for _ in range(n - 1)]
        ops.append("POP %d" % stacks)
    elif mode == 7:
        assert n >= 40 * stacks
        for s in range(1, stacks + 1):
            for _ in range(10):
                ops.append("PUSH %d %d" % (s, rng.randint(0, TOP)))
            sizes[s] = 10
        while len(ops) < n - 20 * stacks:
            s = rng.randint(1, stacks)
            if sizes[s] == 11:
                ops.append("POP %d" % s)
                sizes[s] -= 1
            else:
                ops.append("PUSH %d %d" % (s, rng.randint(0, TOP)))
                sizes[s] += 1
        order = list(range(1, stacks + 1))
        rng.shuffle(order)
        for s in order:
            ops.extend(["POP %d" % s] * sizes[s])
        while len(ops) + 2 <= n:
            s = rng.randint(1, stacks)
            ops.extend(["PUSH %d %d" % (s, rng.randint(0, TOP)), "POP %d" % s])
        if len(ops) < n:
            ops.append("PUSH 1 0")
    if mode in (5, 6, 7):
        sys.stdout.write("\n".join([str(n)] + ops) + "\n")
        return
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
