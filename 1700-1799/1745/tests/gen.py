"""One test from a seed and a mode: mode 1 up to 6 short words, mode 2
1000 words of random brackets, mode 3 1000 words of three kinds whose
order matters, mode 4 a few long words, mode 5 eight shuffled pieces of
a random balanced sequence (optional even total length, default 10000)."""

import random
import sys

FEW = 6
SHORT = 4
MOST = 1000
TOTAL = 10000
LONG = 10
# opening words, closing words with a deep dip, closing words that dip
# only at the end: the deep ones must come before the shallow ones
KINDS = ("(" * 5, ")" * 5 + "(" * 4, "(" * 4 + ")" * 5)


def word(rng, size, bias):
    return "".join("(" if rng.random() < bias else ")" for _ in range(size))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        words = [word(rng, rng.randint(1, SHORT), 0.5) for _ in range(rng.randint(1, FEW))]
    elif mode == 2:
        words = [word(rng, TOTAL // MOST, rng.random()) for _ in range(MOST)]
    elif mode == 3:
        words = [rng.choice(KINDS) for _ in range(MOST)]
    elif mode == 5:
        total = int(sys.argv[3]) if len(sys.argv) > 3 else TOTAL
        count = FEW + 2
        if not count <= total <= TOTAL or total % 2:
            raise ValueError("mode 5 needs an even total length from 8 to 10000")
        brackets = list("(" * (total // 2) + ")" * (total // 2))
        rng.shuffle(brackets)
        depth = low = start = 0
        for i, c in enumerate(brackets):
            depth += 1 if c == "(" else -1
            if depth < low:
                low, start = depth, i + 1
        brackets = brackets[start:] + brackets[:start]
        cuts = [0] + sorted(rng.sample(range(1, total), count - 1)) + [total]
        words = ["".join(brackets[a:b]) for a, b in zip(cuts, cuts[1:])]
        rng.shuffle(words)
    else:
        words = [word(rng, TOTAL // LONG, rng.random()) for _ in range(LONG)]
    print(len(words))
    print("\n".join(words))


main()
