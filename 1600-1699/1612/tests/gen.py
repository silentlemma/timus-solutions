"""One message from a seed and a mode, up to 10000 characters of small
letters, spaces, line breaks and the marks . , - : ! ?. Mode 1 mixes the
two words with near misses such as trams, tramway and trolleybuses,
mode 2 balances them exactly, mode 3 glues them to marks, mode 4 has
neither word."""

import random
import sys

MOST = 10000
NEAR = ["trams", "tramway", "atram", "tra", "trolleybuses", "trolley", "bus", "trolleybusx"]
OTHER = ["the", "best", "driver", "city", "forum", "ride", "route", "depot"]
SEPS = [" ", " ", "\n", ", ", ". ", "! ", "? ", " - ", ": "]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    words = []
    size = 0
    limit = MOST * 4 // 5 if mode == 2 else MOST - 30  # room for the longer words
    while size < limit:
        roll = rng.random()
        if mode in (2, 4):
            w = rng.choice(OTHER + NEAR)
        elif roll < 0.2:
            w = rng.choice(["tram", "trolleybus"])
        elif roll < 0.5:
            w = rng.choice(NEAR)
        else:
            w = rng.choice(OTHER)
        sep = rng.choice(SEPS) if mode != 3 else rng.choice(".,-:!?")
        words.append(w + sep)
        size += len(w) + len(sep)
    if mode == 2:
        # put the same number of both words in place of short words
        short = [i for i, w in enumerate(words) if len(w) <= len("tram") + 1]
        rng.shuffle(short)
        half = len(short) // 2
        for i in short[:half]:
            words[i] = "tram" + words[i][-1]
        for i in short[half : 2 * half]:
            words[i] = "trolleybus" + words[i][-1]
    sys.stdout.write("".join(words).rstrip() + "\n")


main()
