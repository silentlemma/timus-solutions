"""English-like prose: a seed and a mode. Common words are drawn with
falling weights and put into sentences with commas, quotes, questions
and apostrophes, wrapped into lines and paragraphs. Mode 1 gives about
20000 characters, mode 2 about 100000, mode 3 just under 200000, mode 4
about 30000 characters full of dialogue, digits and question marks, mode
5 about 25000 characters with odd symbols, backslashes included (the
legacy output includes a final newline). Modes 6, 7 and 8 give exactly
200000 characters: wrapped prose, one line with escape-heavy annotations,
and short lines separated by blank lines, respectively. Mode 9 gives
137111 characters with irregular paragraph widths and no final newline."""

import random
import sys

WORDS = (
    "the of and to a in that he was it his is with as i had for at by on not be "
    "but from her which or have she they you all were this so one are an my been "
    "him their there when if we what would who will said no them more out up into "
    "do then me could your about any now some time very like upon man little only "
    "other its than can great old good well before made over down such these should "
    "after first two must see where much our those know way way never us long come "
    "again house night eyes face hand head door room water light world life heart "
    "thought looked away young without nothing something every through still under "
    "himself herself against between while because once think another people place"
).split()
NAMES = ["Elizabeth", "Darcy", "Holmes", "Watson", "Alice", "Ishmael", "Emma", "Pip"]
LINE = 72
TARGET = {1: 20500, 2: 100000, 3: 199000, 4: 30000, 5: 25000}
ODD = "#$%&*+<=>@[]^_`{|}~\\/"


def sentence(rng, mode):
    words = []
    for i in range(rng.randint(4, 18)):
        if rng.random() < 0.05:
            words.append(rng.choice(NAMES))
        else:
            k = min(int(rng.paretovariate(1.1)) - 1, len(WORDS) - 1)
            words.append(WORDS[k])
        if i > 2 and rng.random() < 0.08:
            words[-1] += ","
        if rng.random() < 0.02:
            words[-1] += "'s"
    if mode == 5 and rng.random() < 0.3:
        words.append(rng.choice(ODD) * rng.randint(1, 3))
    if mode == 4 and rng.random() < 0.2:
        words.append(str(rng.randint(1, 1900)))
    words[0] = words[0].capitalize()
    end = rng.choice("...!???" if mode == 4 else "..........!?")
    text = " ".join(words) + end
    if rng.random() < (0.5 if mode == 4 else 0.15):
        text = '"' + text + '"'
    return text


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7, 8, 9):
        extended(rng, mode)
        return
    paragraphs, size = [], 0
    while size < TARGET[mode]:
        words = " ".join(sentence(rng, mode) for _ in range(rng.randint(2, 7))).split(" ")
        lines, line = [], ""
        for w in words:
            if line and len(line) + 1 + len(w) > LINE:
                lines.append(line)
                line = w
            else:
                line = (line + " " + w) if line else w
        lines.append(line)
        paragraphs.append("\n".join(lines))
        size += sum(len(x) + 1 for x in lines) + 1
    sys.stdout.write("\n\n".join(paragraphs) + "\n")


def extended(rng, mode):
    import textwrap

    target = 137111 if mode == 9 else 200000
    parts, size = [], 0
    while size < target:
        text = " ".join(sentence(rng, 4) for _ in range(rng.randint(2, 6)))
        if mode == 7:
            text += ' The note read: "??/ ??= ??!" beside C:\\books\\novel. '
        elif mode == 8:
            text = "\n\n".join(textwrap.wrap(text, 20)) + "\n\n"
        else:
            width = 72 if mode == 6 else rng.randint(30, 120)
            text = "\n".join(textwrap.wrap(text, width)) + "\n\n"
        parts.append(text)
        size += len(text)
    text = "".join(parts)[:target - 1]
    text += "." if mode == 9 else "\n"
    # Binary output avoids Windows newline translation in these new modes.
    sys.stdout.buffer.write(text.encode("ascii"))


main()
