"""A line of brackets: a seed, its length and a mode. Mode 0 is random,
mode 1 a regular sequence with some brackets removed, mode 2 only opening
brackets, mode 3 crossed pairs like ([)]."""

import random
import sys

DROP = 0.2


def regular(rng, n):
    out, stack = [], []
    while len(out) + len(stack) < n:
        if stack and (rng.random() < 0.5 or len(out) + 2 * len(stack) >= n):
            out.append(")" if stack.pop() == "(" else "]")
        else:
            c = rng.choice("([")
            stack.append(c)
            out.append(c)
    while stack:
        out.append(")" if stack.pop() == "(" else "]")
    return out


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        s = [c for c in regular(rng, n) if rng.random() > DROP]
    elif mode == 2:
        s = [rng.choice("([") for _ in range(n)]
    elif mode == 3:
        s = list("([)]" * (n // 4))
    else:
        s = [rng.choice("()[]") for _ in range(n)]
    sys.stdout.write("".join(s[:n]) + "\n")


if __name__ == "__main__":
    main()
