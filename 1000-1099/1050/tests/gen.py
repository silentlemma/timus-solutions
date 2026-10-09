"""A random text: a seed, the number of lines and 1 to end without a final
line break. Lines are at most 80 characters of Latin and Cyrillic words,
quotes, umlauts \\", commands \\par and \\parbox, backslash pairs (always
followed by a space), single quotes and spaces; some lines are blank or
hold only spaces and tabs.
The last line is \\endinput."""

import random
import sys

WIDTH = 80
PIECES = [
    '"',
    '"',
    '"',
    '\\"',
    "\\par",
    "\\par ",
    "\\parbox",
    "\\\\ ",
    "``",
    "''",
    "`",
    "'",
    " ",
    " ",
    "-",
    ",",
    ".",
    "\\thinspace",
]
LATIN = "abcdefghijklmnopqrstuvwxyz"
CYRILLIC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВЕЁЖЗ«»№"


def word(rng):
    letters = LATIN if rng.randrange(2) else CYRILLIC
    return "".join(rng.choice(letters) for _ in range(rng.randint(1, 8)))


def main():
    seed, count = int(sys.argv[1]), int(sys.argv[2])
    no_final_break = len(sys.argv) > 3 and sys.argv[3] == "1"
    rng = random.Random(seed)
    lines = []
    for _ in range(count - 1):
        kind = rng.randrange(10)
        if kind == 0:
            lines.append("")
        elif kind == 1:
            lines.append("".join(rng.choice(" \t") for _ in range(rng.randint(1, 5))))
        else:
            line = ""
            while True:
                piece = word(rng) if rng.randrange(3) == 0 else rng.choice(PIECES)
                if len(line) + len(piece) > WIDTH:
                    break
                line += piece
            lines.append(line)
    lines.append("\\endinput")
    sys.stdout.write("\n".join(lines) + ("" if no_final_break else "\n"))


if __name__ == "__main__":
    main()
