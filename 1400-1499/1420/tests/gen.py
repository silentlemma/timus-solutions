"""One complex-division input from a seed and a mode.

Mode 1: random parts in [-30, 30], with a nonzero divisor.
Mode 2: random parts over the full allowed range, with a nonzero divisor.
Mode 3: random signs and parts within 32 of the maximum absolute value.
"""

import random
import sys

LIMIT = 10**6


def main():
    seed, mode = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode in (1, 2):
        bound = 30 if mode == 1 else LIMIT
        parts = [rng.randint(-bound, bound) for _ in range(4)]
        while parts[2:] == [0, 0]:
            parts[2:] = [rng.randint(-bound, bound) for _ in range(2)]
    elif mode == 3:
        parts = [rng.choice((-1, 1)) * (LIMIT - rng.randrange(33)) for _ in range(4)]
    else:
        raise ValueError('unknown mode')
    sys.stdout.buffer.write(f'{parts[0]} {parts[1]}\n{parts[2]} {parts[3]}\n'.encode())


if __name__ == '__main__':
    main()
