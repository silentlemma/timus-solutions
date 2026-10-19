"""A poem from a seed and a mode: mode 1 a few lines in one meter, 2 the
most lines in one meter, 3 the most lines with one syllable of one line
stressed wrongly, 4 the most lines with one line in another meter,
5 the most lines with two spaces between some words. Lines are cut into
words of one to four syllables of one to three letters and kept within
50 characters."""

import random
import string
import sys

MOST = 100
LONGEST = 50
FEW = 4
LETTERS = 3
METERS = [(2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]


def syllable(rng, stressed):
    letters = "".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, LETTERS)))
    return "[%s]" % letters if stressed else letters


def verse(rng, marks, wide):
    # cut the syllables into words; None when the line is too long
    words, i = [], 0
    while i < len(marks):
        size = min(len(marks) - i, rng.randint(1, FEW))
        words.append([syllable(rng, s) for s in marks[i:i + size]])
        i += size
    line = ""
    for k, word in enumerate(words):
        if k:
            line += "  " if wide and rng.random() < 0.5 else " "
        line += "-".join(word)
    return line if len(line) <= LONGEST else None


def meter_line(rng, foot, place, wide, flip=False):
    while True:
        count = rng.randint(FEW, LONGEST // 2)
        marks = [i % foot == place for i in range(count)]
        if flip:
            k = rng.randrange(count)
            marks[k] = not marks[k]
        line = verse(rng, marks, wide)
        if line:
            return line


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode == 1 else MOST
    foot, place = rng.choice(METERS)
    lines = [meter_line(rng, foot, place, mode == 5) for _ in range(n)]
    odd = rng.randrange(n)
    if mode == 3:
        lines[odd] = meter_line(rng, foot, place, False, True)
    if mode == 4:
        other = rng.choice([m for m in METERS if m != (foot, place)])
        lines[odd] = meter_line(rng, other[0], other[1], False)
    print(n)
    print("\n".join(lines))


main()
