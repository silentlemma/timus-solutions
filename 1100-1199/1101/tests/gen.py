"""A random field: a seed, N, M, K, the depth of the expression and the
number of registers used. Fields where the robot would not leave within
a bound are skipped."""

import random
import sys

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LIMIT = 200000
MAX_LENGTH = 250


def expression(rng, depth, regs):
    if depth == 0 or rng.random() < 0.2:
        return rng.choice(regs + ["TRUE", "FALSE"] if rng.random() < 0.2 else regs)
    kind = rng.randrange(4)
    if kind == 0:
        return "NOT" + rng.choice([" ", ""]) * 1 + "(" + expression(rng, depth - 1, regs) + ")"
    if kind == 1:
        return "NOT " + expression(rng, depth - 1, regs)
    op = rng.choice([" AND ", " OR "])
    inner = expression(rng, depth - 1, regs) + op + expression(rng, depth - 1, regs)
    return "(" + inner + ")" if rng.random() < 0.5 else inner


def evaluate(expr, reg):
    words = {"NOT": "not", "AND": "and", "OR": "or", "TRUE": "True", "FALSE": "False"}
    code = []
    word = ""
    for ch in expr + " ":
        if ch.isalpha():
            word += ch
            continue
        if word:
            code.append(words.get(word, "reg[%r]" % word))
            word = ""
        if ch in "()":
            code.append(ch)
    return eval(" ".join(code), {}, {"reg": reg})


def walk(rng, expr, n, m, k, regs):
    """Walks the robot and puts forks and switches on cells it reaches for
    the first time, so that they matter; None if it does not leave."""
    reg = {c: False for c in LETTERS}
    forks, inv, seen = [], {}, {(0, 0)}
    x = y = 0
    dx, dy = 1, 0
    for _ in range(LIMIT):
        if not (-n <= x <= n and -n <= y <= n):
            return forks, inv
        if (x, y) not in seen:
            seen.add((x, y))
            roll = rng.random()
            if roll < 0.25 and len(forks) < m:
                forks.append((x, y))
            elif roll < 0.4 and len(inv) < k:
                inv[(x, y)] = rng.choice(regs)
        if (x, y) in inv:
            reg[inv[(x, y)]] = not reg[inv[(x, y)]]
        if (x, y) in forks:
            dx, dy = (dy, -dx) if evaluate(expr, reg) else (-dy, dx)
        x, y = x + dx, y + dy
    return None


def main():
    seed, n, m, k, depth, used = (int(x) for x in sys.argv[1:7])
    rng = random.Random(seed)
    regs = list(LETTERS[:used])
    while True:
        expr = expression(rng, depth, regs)
        if len(expr) > MAX_LENGTH:
            continue
        found = walk(rng, expr, n, m, k, regs)
        if found:
            forks, inv = found
            break
    lines = [expr, "%d %d %d" % (n, len(forks), len(inv))] + ["%d %d" % p for p in forks]
    lines += ["%d %d %s" % (p[0], p[1], c) for p, c in inv.items()]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
