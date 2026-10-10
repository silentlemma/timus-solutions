"""N comparisons with random strings and patterns over a small alphabet: a
seed, N, the longest string and a mode. Mode 0 draws patterns from
letters, %, _ and bracket sets, mode 1 copies the string into the pattern
and then garbles it, mode 2 also uses quotes, ^, - and bytes above 127,
including unclosed brackets. Quotes are doubled; the file is written in
UTF-8 and the tests turn it into Latin-1 bytes."""

import random
import sys

LETTERS = "ab"
EXTRA = "'^-[]%_" + chr(200) + chr(255)


def piece(rng, alphabet):
    r = rng.random()
    if r < 0.15:
        return "%"
    if r < 0.25:
        return "_"
    if r < 0.45:
        body = "^" if rng.random() < 0.3 else ""
        for _ in range(rng.randint(0, 3)):
            a = rng.choice(alphabet)
            body += a + "-" + rng.choice(alphabet) if rng.random() < 0.3 else a
        return "[" + body + "]"
    return rng.choice(alphabet)


def quote(s):
    return "'" + s.replace("'", "''") + "'"


def main():
    seed, n, longest, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    alphabet = LETTERS + (EXTRA if mode == 2 else "")
    lines = [str(n)]
    for _ in range(n):
        text = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, longest)))
        if mode == 1:
            pattern = "".join(c if rng.random() < 0.7 else piece(rng, alphabet) for c in text)
        else:
            pattern = ""
            while len(pattern) < rng.randint(0, longest):
                pattern += piece(rng, alphabet)
        if mode == 2 and rng.random() < 0.1:
            pattern += "["
        pattern = pattern[:longest]
        lines.append("%s like %s" % (quote(text), quote(pattern)))
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
