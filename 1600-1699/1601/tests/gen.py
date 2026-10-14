"""One message from a seed and a mode, up to 10000 characters of capital
letters, spaces, line breaks and the marks . , - : ! ?. Mode 1 is random
words and sentences, mode 2 puts marks right next to letters, mode 3 is
a single long sentence across many lines, mode 4 a short message."""

import random
import string
import sys

MOST = 10000
SHORT = 60
MARKS = ".,-:!?"


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    limit = SHORT if mode == 4 else MOST
    out = []
    size = 0
    while True:
        word = "".join(rng.choice(string.ascii_uppercase) for _ in range(rng.randint(1, 8)))
        if mode == 2:
            sep = rng.choice(MARKS) + rng.choice(["", " ", "\n"])
        elif mode == 3:
            sep = rng.choice([" ", " ", "\n", ", ", " - ", ": "])
        else:
            sep = rng.choice([" ", " ", " ", ", ", ". ", "! ", "? ", ".\n", " - ", ": ", "\n"])
        if size + len(word) + len(sep) > limit - 1:
            break
        out.append(word + sep)
        size += len(word) + len(sep)
    text = "".join(out).rstrip("\n") + ("." if mode == 3 else "")
    sys.stdout.write(text + "\n")


main()
