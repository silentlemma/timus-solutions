"""One test from a seed and a mode: a song and a log of presses at least
50 ms apart. Mode 1 takes a random song and player, mode 2 a long Hard
song, mode 3 a short song with few steps, mode 4 a player who mostly
hits on time, mode 5 a player who presses wrong keys and misses, and
mode 6 a longest Hard song with every beat Perfect and presses every 50 ms."""

import random
import sys

LEVELS = (("Easy", 1000), ("Medium", 500), ("Hard", 250))
KEYS = "UDLR"
SHORTEST, LONGEST = 10, 599  # seconds
GAP = 50  # ms between presses at least
MS = 1000


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 6:
        period = LEVELS[2][1]
        song = "".join(rng.choice(KEYS) for _ in range(LONGEST * MS // period))
        print("%d:%02d Hard" % (LONGEST // 60, LONGEST % 60))
        print(song)
        for t in range(0, LONGEST * MS, GAP):
            beat = song[t // period]
            key = beat if t % period == 0 else rng.choice(KEYS.replace(beat, ""))
            print(t, key)
        return
    level, period = LEVELS[2] if mode == 2 else rng.choice(LEVELS)
    seconds = LONGEST if mode == 2 else (SHORTEST if mode == 3 else rng.randint(SHORTEST, LONGEST))
    beats = seconds * MS // period
    empty = rng.uniform(0.0, 0.9)
    song = [rng.choice(KEYS) if rng.random() > empty else "N" for _ in range(beats)]
    if all(b == "N" for b in song):
        song[rng.randrange(beats)] = rng.choice(KEYS)
    skill = {4: 0.95, 5: 0.3}.get(mode, rng.random())
    log = []
    last = -GAP
    for i, b in enumerate(song):
        start = i * period
        presses = rng.choice((0, 1, 1, 1, 2)) if b != "N" else rng.choice((0, 0, 0, 1))
        for _ in range(presses):
            low = max(start, last + GAP)
            if low >= start + period:
                break
            t = rng.randint(low, start + period - 1)
            if mode == 4 and b != "N":
                t = rng.randint(low, min(start + period - 1, low + period // 2))
            key = b if b != "N" and rng.random() < skill else rng.choice(KEYS)
            log.append((t, key))
            last = t
    print("%d:%02d %s" % (seconds // 60, seconds % 60, level))
    print("".join(song))
    for t, key in log:
        print(t, key)


main()
