"""Phrases near the input limits: a seed and a mode. Mode 1 is 10 000
distinct words of 1 to 50 letters on many lines with mixed separators,
mode 2 is 5 000 words of 100 letters, mode 3 has word lengths that rise
and fall so that greedy choices fail, mode 4 has long separator runs,
blank lines and CRLF line ends."""

import random
import string
import sys

SEPARATORS = " ,.!?-_=*'0123456789\t"
LETTERS = string.ascii_letters


def words(rng, count, lengths, seen=None):
    if seen is None:
        seen = set()
    result = []
    while len(result) < count:
        word = "".join(rng.choice(LETTERS) for _ in range(rng.choice(lengths)))
        if word.lower() not in seen:
            seen.add(word.lower())
            result.append(word)
    return result


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        phrase = words(rng, 10000, range(1, 51))
        parts = []
        for word in phrase:
            parts.append(word)
            parts.append("\n" if rng.random() < 0.05 else rng.choice(SEPARATORS))
        sys.stdout.write("".join(parts))
    elif mode == 2:
        print(" ".join(words(rng, 5000, [100])))
    elif mode == 3:
        lengths = [3 + abs(i % 40 - 20) * 4 + rng.randint(0, 2) for i in range(8000)]
        seen = set()
        phrase = [words(rng, 1, [n], seen)[0] for n in lengths]
        print(" ".join(phrase))
    else:
        phrase = words(rng, 3000, range(3, 30))
        parts = []
        for word in phrase:
            parts.append(word)
            parts.append("".join(rng.choice(SEPARATORS) for _ in range(rng.randint(1, 30))))
            if rng.random() < 0.1:
                parts.append("\r\n\r\n")
        sys.stdout.buffer.write("".join(parts).encode())


main()
