"""Generate a program from a seed and a mode (at most 2000 lines).

Mode 1: an endless loop of random commands in three safe integer ranges.
Mode 2: the same with mixed case, spaces, empty lines and label-only lines.
Mode 3: 1999 distinct assigned variables followed by an endless self-jump.
Mode 4: a terminating random program with forward branches and variable divisors.
"""

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


def indexed_name(index):
    suffix = ""
    for _ in range(3):
        suffix = string.ascii_lowercase[index % 26] + suffix
        index //= 26
    return "v" + suffix


def many_variables(rng):
    for i in range(LINES - 1):
        print(f"{indexed_name(i)} = {rng.randint(-(2**31), 2**31 - 1)}")
    print("stop: goto STOP")


def finite_random(rng):
    names = ["alpha", "Beta", "gamma", "Delta"]
    lines = [f"{name} = {rng.randint(-10000, 10000)}" for name in names]
    lines.append(f"divisor = {rng.choice([-1, 1]) * rng.randint(1, 999)}")
    for i in range(200):
        dest = rng.choice(names)
        op = rng.choice(["+", "-", "*", "/", "%", "and", "or", "xor", "not", "copy"])
        left = rng.choice(names + [str(rng.randint(-10000, 10000))])
        right = str(rng.randint(-10000, 10000))
        if op in ("/", "%"):
            right = "divisor"
        elif op == "*":
            left, right = str(rng.randint(-10000, 10000)), str(rng.randint(-10000, 10000))
        if op == "not":
            expression = f"not {left}"
        elif op == "copy":
            expression = left
        else:
            expression = f"{left} {op} {right}"
        label = "skip" + indexed_name(i)
        comparison = rng.choice(["==", "!=", "<", ">", "<=", ">="])
        lines += [
            f"{dest} = {expression}",
            f"if {dest} {comparison} {right} goto {label}",
            f"{dest} = not {dest}",
            f"{label}: print {dest}",
        ]
    lines.append("end")
    print("\n".join(lines))


def word(rng, taken):
    while True:
        w = "".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, LONGEST)))
        if w.lower() not in taken:
            taken.add(w.lower())
            return w


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        many_variables(rng)
        return
    if mode == 4:
        finite_random(rng)
        return
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
