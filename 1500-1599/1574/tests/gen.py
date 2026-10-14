"""One test from a seed and a mode: a bracket line of up to 100000
characters. Mode 1 rotates a random balanced line, mode 2 repeats "()",
mode 3 is unbalanced by two, mode 4 is a deep nest rotated, mode 5 short
random."""

import random
import sys

LONGEST = 100000
SHORT = 12


def balanced(rng, half):
    """A random balanced line with half pairs."""
    out, opened, left = [], 0, half
    while left or opened:
        if left and (not opened or rng.random() < 0.5):
            out.append("(")
            opened += 1
            left -= 1
        else:
            out.append(")")
            opened -= 1
    return "".join(out)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        line = balanced(rng, LONGEST // 2)
    elif mode == 2:
        line = "()" * (LONGEST // 2)
    elif mode == 3:
        line = balanced(rng, LONGEST // 2 - 1) + "(("
    elif mode == 4:
        line = "(" * (LONGEST // 2) + ")" * (LONGEST // 2)
    else:
        line = "".join(rng.choice("()") for _ in range(rng.randint(1, SHORT)))
    cut = rng.randrange(len(line))
    print(line[cut:] + line[:cut])


main()
