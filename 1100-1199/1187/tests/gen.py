"""A survey: a seed, the number of questions, the number of result lines,
the number of cross tables and a mode. Mode 0 draws answers uniformly,
mode 1 makes most people pick the same few answers, so many rows and
columns are empty, mode 2 uses only two answers per question."""

import random
import string
import sys

CODES = string.ascii_uppercase + string.digits + ".*@"
WORDS = ["Yes", "No", "Maybe", "Hello!", "(other)", "Fine", "Who", "are", "you", "really"]
MOST_ANSWERS = 10


def name(rng, longest):
    text = " ".join(rng.choice(WORDS) for _ in range(rng.randint(1, 6)))
    return text[:longest].strip() or "X"


def main():
    seed, questions, people, tables, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    codes = set()
    while len(codes) < questions:
        codes.add("".join(rng.choice(string.ascii_uppercase + string.digits) for _ in range(3)))
    codes = sorted(codes)
    rng.shuffle(codes)
    lines = ["Survey " + name(rng, 90)]
    answers = []
    for code in codes:
        size = 2 if mode == 2 else rng.randint(2, MOST_ANSWERS)
        options = rng.sample(CODES, size)
        answers.append(options)
        lines.append("%s %s" % (code, name(rng, 80)))
        lines += [" %s %s" % (a, name(rng, 40)) for a in options]
    lines.append("#")
    for _ in range(people):
        if mode == 1:
            lines.append(
                "".join(o[0] if rng.random() < 0.8 else rng.choice(o[:2]) for o in answers)
            )
        else:
            lines.append("".join(rng.choice(o) for o in answers))
    lines.append("#")
    for _ in range(tables):
        a, b = rng.sample(codes, 2)
        lines.append("%s %s %s" % (a, b, name(rng, 100)))
    lines.append("#")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
