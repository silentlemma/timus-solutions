"""Lines of expressions from a seed and a mode, at most 50 characters each,
with every value along the way within 0 .. 10^9. Mode 1 nests operations,
brackets and glued terms, mode 2 adds a stray character to them, mode 3
writes short random strings over the allowed characters, mode 4 puts a
dozen small numbers under one operation."""

import random
import sys

LINES = 1000
WIDTH = 50
LIMIT = 10**9
DEPTH = 3
CHARS = "0123456789+*/();"


class Check:
    """Evaluates like the solutions and fails on a value out of range."""

    def __init__(self, s):
        self.s, self.pos = s, 0

    def keep(self, v):
        if not 0 <= v <= LIMIT:
            raise ValueError
        return v

    def accept(self, c):
        if self.pos < len(self.s) and self.s[self.pos] == c:
            self.pos += 1
            return True
        return False

    def term(self):
        s = self.s
        if self.pos < len(s) and s[self.pos].isdigit():
            start = self.pos
            while self.pos < len(s) and s[self.pos].isdigit():
                self.pos += 1
            return self.keep(int(s[start : self.pos]))
        for sign in "+*/":
            if self.accept(sign):
                a = self.glue(True)
                while self.accept(";"):
                    b = self.glue(True)
                    if sign == "+":
                        a += b
                    elif sign == "*":
                        a *= b
                    else:
                        a = 0 if b == 0 else a // b
                    self.keep(a)
                return a
        if self.accept("("):
            x = self.glue(False)
            self.accept(")")
            return x
        return -1

    def glue(self, inside):
        parts = []
        x = self.term()
        while x != -1 or not parts:
            parts.append(x)
            if self.pos < len(self.s) and self.s[self.pos] == ";":
                if inside:
                    break
                self.pos += 1
                parts.append(self.glue(False))
            x = self.term()
        return self.keep(int("".join(str(abs(p)) for p in parts)))


def nested(rng, depth):
    roll = rng.random()
    if depth > DEPTH or roll < 0.35:
        return str(rng.choice([0, 1, 2, 3, 5, 7, 10, 12, 99, rng.randint(0, 999)]))
    if roll < 0.7:
        args = [nested(rng, depth + 1) for _ in range(rng.randint(1, 3))]
        return rng.choice("+*/") + ";".join(args)
    if roll < 0.85:
        return "(" + nested(rng, depth + 1) + ")"
    return nested(rng, depth + 1) + rng.choice(["", ";"]) + nested(rng, depth + 1)


def line(rng, mode):
    if mode == 3:
        return "".join(rng.choice(CHARS) for _ in range(rng.randint(0, 12)))
    if mode == 4:
        return rng.choice("+*/") + ";".join(str(rng.randint(1, 3)) for _ in range(12))
    e = nested(rng, 0)
    if mode == 2:
        i = rng.randrange(len(e) + 1)
        e = e[:i] + rng.choice(CHARS) + e[i:]
    return e[:WIDTH]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    while len(lines) < LINES:
        e = line(rng, mode)
        try:
            Check(e).glue(False)
        except ValueError:
            continue
        lines.append(e)
    print("\n".join(lines))


main()
