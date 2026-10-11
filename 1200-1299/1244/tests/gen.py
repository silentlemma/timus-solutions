"""A deck and the weight of what is left: a seed, N and a mode. Mode 1
draws card weights at random and leaves out random cards, which nearly
always has many answers; mode 2 leaves out one card lighter than all the
others, so only that card can be missing; mode 3 draws weights from a few
values, so many sets tie."""

import random
import sys

TOP = 1000
FEW = 3


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 2:
        light = rng.randint(1, TOP // 2)
        cards = [rng.randint(light + 1, TOP) for _ in range(n)]
        lost = rng.randrange(n)
        cards[lost] = light
        weight = sum(cards) - light
    else:
        if mode == 3:
            values = [rng.randint(1, TOP) for _ in range(FEW)]
            cards = [rng.choice(values) for _ in range(n)]
        else:
            cards = [rng.randint(1, TOP) for _ in range(n)]
        weight = sum(c for c in cards if rng.random() < 0.5)
        weight = min(max(weight, 1), sum(cards) - 1)
    sys.stdout.write("%d\n%d\n%s\n" % (weight, n, "\n".join(map(str, cards))))


if __name__ == "__main__":
    main()
