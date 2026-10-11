"""Generate one seeded robot decision: MODE SEED.

random: all non-angle fields range from 0 to 1000, with boundary-heavy angles.
small: counts up to 8 and resources/powers up to 30, with boundary-heavy angles.
"""

import random
import sys

ANGLES = (-179, -161, -160, -91, -90, -89, -21, -20, -10, -9, -5, -4,
          0, 4, 5, 9, 10, 20, 21, 89, 90, 91, 159, 160, 161, 180)


def generate(mode, seed):
    rng = random.Random(seed)
    limit, count_limit = (30, 8) if mode == "small" else (1000, 1000)

    def angle():
        return rng.choice(ANGLES) if rng.randrange(2) else rng.randint(-179, 180)

    energy, ammo = rng.randint(0, limit), rng.randint(0, limit)
    behaviour = rng.choice("GDAP")
    enemies, power = rng.randint(0, count_limit), rng.randint(0, limit)
    lines = [f"{energy} {ammo}", behaviour, f"{enemies} {power} {angle()}"]
    if behaviour == "A":
        lines.append(f"{rng.randint(0, count_limit)} {rng.randint(0, limit)}")
    elif behaviour == "P":
        lines.append(str(angle()))
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("random", "small"):
        raise SystemExit("usage: gen.py {random|small} SEED")
    sys.stdout.write(generate(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
