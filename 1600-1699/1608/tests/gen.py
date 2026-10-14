"""One test from SEED MODE.

random: two uniform endpoints over the entire allowed range, sorted.
lucky-window: a short interval around a random lucky 18-digit ticket.
"""

import random
import sys

MAX_VALUE = 10**18


def main():
    seed, mode = sys.argv[1:]
    rng = random.Random(int(seed))
    if mode == "random":
        a, b = sorted(rng.randint(1, MAX_VALUE) for _ in range(2))
    elif mode == "lucky-window":
        digits = [rng.randrange(1, 10)] + [rng.randrange(10) for _ in range(8)]
        digits += [rng.choice([d for d in range(10) if d != left])
                   for left in reversed(digits)]
        ticket = int("".join(map(str, digits)))
        a = ticket - rng.randrange(1, 101)
        b = ticket + rng.randrange(1, 101)
    else:
        raise SystemExit(f"unknown mode: {mode}")
    print(a, b)


if __name__ == "__main__":
    main()
