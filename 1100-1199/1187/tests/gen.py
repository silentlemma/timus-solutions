"""A survey: a seed, the number of questions, the number of result lines,
the number of cross tables and a mode. Mode 0 draws answers uniformly,
mode 1 makes most people pick the same few answers, so many rows and
columns are empty, mode 2 uses only two answers per question, mode 3
uses ten answers and maximum-length names throughout, and mode 4
uses ten answers with nine rare respondents and a dominant answer.
Modes 3 and 4 require at least ten people. All modes take the same five
integer arguments: seed, questions, people, tables, mode."""

import random
import string
import sys

CODES = string.ascii_uppercase + string.digits + ".*@"
WORDS = ["Yes", "No", "Maybe", "Hello!", "(other)", "Fine", "Who", "are", "you", "really"]
MOST_ANSWERS = 10


def name(rng, longest):
    text = " ".join(rng.choice(WORDS) for _ in range(rng.randint(1, 6)))
    return text[:longest].strip() or "X"


def extended(seed, questions, people, tables, mode):
    assert 2 <= questions <= 100 and 10 <= people and questions * people <= 10000
    assert 1 <= tables <= 100 and mode in (3, 4)
    rng = random.Random(seed)
    codes = rng.sample(["%03d" % i for i in range(1000)], questions)
    options = [rng.sample(CODES, MOST_ANSWERS) for _ in codes]

    def label(prefix, length):
        return (prefix + " " + "X" * length)[:length]

    lines = [label("Maximum survey", 100) if mode == 3 else "Rare answer survey"]
    for code, answers in zip(codes, options):
        lines.append(code + " " + label("Question " + code, 80))
        lines.extend(" %s %s" % (a, label("Answer " + a, 40)) for a in answers)
    lines.append("#")
    rare = []
    for _ in codes:
        order = list(range(1, MOST_ANSWERS))
        rng.shuffle(order)
        rare.append(order)
    for person in range(people):
        if mode == 3:
            lines.append("".join(rng.choice(o) for o in options))
        elif person < people - (MOST_ANSWERS - 1):
            lines.append("".join(o[0] for o in options))
        else:
            index = person - (people - (MOST_ANSWERS - 1))
            lines.append("".join(o[r[index]] for o, r in zip(options, rare)))
    lines.append("#")
    for table in range(tables):
        a, b = rng.sample(codes, 2)
        lines.append("%s %s %s" % (a, b, label("Table %d" % (table + 1), 100)))
    lines.append("#")
    sys.stdout.write("\n".join(lines) + "\n")


def main():
    seed, questions, people, tables, mode = (int(x) for x in sys.argv[1:6])
    if mode in (3, 4):
        extended(seed, questions, people, tables, mode)
        return
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
