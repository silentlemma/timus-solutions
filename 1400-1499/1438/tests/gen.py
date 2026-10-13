"""An endless loop of random commands, up to 2000 lines: a seed and a mode.
The variables live in three ranges so that no value leaves 32 bits. Mode 2
also mixes letter cases in keywords and labels and adds spaces, empty lines
and lines with only a label."""

import random
import string
import sys

LINES = 2000
COMMANDS = {1: 2000, 2: 1800}
COUNTS = {"big": 8, "mid": 6, "small": 6}
TOP = {"big": 2**31 - 1, "mid": 10**6, "small": 999}
DIVISOR = 1000
PRINTS = 5
LABEL_SHARE = 0.1
LONGEST = 6


def word(rng, taken):
    while True:
        w = "".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, LONGEST)))
        if w.lower() not in taken:
            taken.add(w.lower())
            return w


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    taken = {"end", "print", "goto", "if", "not", "or", "and", "xor", "top"}
    tiers = {t: [word(rng, taken) for _ in range(c)] for t, c in COUNTS.items()}
    every = sum(tiers.values(), [])

    def key(s):
        if mode != 2:
            return s
        return "".join(c.upper() if rng.random() < 0.5 else c for c in s)

    def gap():
        return " " * rng.randint(1, 3) if mode == 2 else " "

    def const(top):
        return str(rng.randint(-top, top))

    def divisor():
        return str(rng.choice([-1, 1]) * rng.randint(1, DIVISOR))

    def anything():
        return rng.choice(every) if rng.random() < 0.8 else const(TOP["mid"])

    def command():
        big, mid, small = tiers["big"], tiers["mid"], tiers["small"]
        roll = rng.random()
        if roll < 0.1:
            return [
                key("if"),
                anything(),
                rng.choice(["==", "!=", ">=", ">", "<=", "<"]),
                anything(),
            ]
        if roll < 0.2:
            return [rng.choice(small), "=", anything(), "%", divisor()]
        if roll < 0.35:
            a, b = (rng.choice(small + [const(TOP["small"])]) for _ in range(2))
            return [rng.choice(mid), "=", a, rng.choice("+-*"), b]
        if roll < 0.45:
            return [rng.choice(mid), "=", rng.choice(mid), "/", divisor()]
        if roll < 0.55:
            return [rng.choice(big), "=", rng.choice(mid), "*", rng.choice(small)]
        if roll < 0.65:
            return [rng.choice(big), "=", key("not"), rng.choice(every)]
        if roll < 0.7:
            return [rng.choice(big), "=", anything()]
        op = key(rng.choice(["or", "and", "xor"]))
        return [rng.choice(big), "=", anything(), op, anything()]

    lines = []
    for t, names in tiers.items():
        lines += [[n, "=", const(TOP[t])] for n in names]
    lines += [[key("print"), rng.choice(every)] for _ in range(PRINTS)]
    start = len(lines)
    body = COMMANDS[mode] - start - 1
    labels = [word(rng, taken) if rng.random() < LABEL_SHARE else None for _ in range(body)]
    labels[0] = "top"
    for i in range(body):
        c = command()
        if c[0].lower() == "if":
            later = [k for k in range(i + 1, body) if labels[k]]
            if later:
                c += [key("goto"), key(labels[rng.choice(later)])]
            else:
                c = [rng.choice(tiers["big"]), "=", c[1]]
        lines.append(c)
    lines.append([key("goto"), key("top")])
    labels = [None] * start + labels + [None]
    out = []
    for label, c in zip(labels, lines):
        if mode == 2 and label and rng.random() < 0.5:
            out.append(gap() + key(label) + ":" + gap())
            label = None
        if mode == 2 and rng.random() < 0.05:
            out.append(gap())
        head = key(label) + ":" + gap() if label else ""
        out.append((gap() if mode == 2 else "") + head + gap().join(c))
    assert len(out) <= LINES
    print("\n".join(out))


main()
