"""One seeded throw: MODE SEED.

random: integer speed, fractional angle, and moderate energy loss.
elastic: small integer speed and angle, with K fixed at 1.0001.
"""

import random
import sys


def main():
    sys.stdout.reconfigure(newline='\n')
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    if mode == 'random':
        v = rng.randint(2, 500000)
        angle = rng.randint(1001, 88999)
        k = rng.randint(125, 1000)
        print(f'{v} {angle // 1000}.{angle % 1000:03d} {k // 100}.{k % 100:02d}')
    elif mode == 'elastic':
        print(f'{rng.randint(2, 100)} {rng.randint(2, 88)} 1.0001')
    else:
        raise SystemExit('usage: gen.py {random|elastic} SEED')


if __name__ == '__main__':
    main()
