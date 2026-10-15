"""One test from a seed and a mode: mode 1 a few short commands over
"ab", mode 2 1000 commands of length 100 over "ab", mode 3 1000 random
commands over a few letters, mode 4 near copies of one long command.
Commands that are substrings of others are dropped."""

import random
import sys

MOST = 1000
LONGEST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        count, letters, low, high = rng.randint(2, 6), "ab", 1, 6
    elif mode == 2:
        count, letters, low, high = MOST, "ab", LONGEST, LONGEST
    else:
        count, letters, low, high = MOST, "abc", 1, LONGEST
    base = "".join(rng.choice("ab") for _ in range(LONGEST))
    words = []
    seen = set()
    while len(words) < count:
        if mode == 4:
            w = list(base)
            for _ in range(rng.randint(1, 3)):
                w[rng.randrange(LONGEST)] = rng.choice("abc")
            w = "".join(w)
        else:
            w = "".join(rng.choice(letters) for _ in range(rng.randint(low, high)))
        if w in seen:
            continue
        if mode == 1 and len(words) > 0 and rng.random() < 0.3:
            continue
        seen.add(w)
        words.append(w)
        if mode != 1 and len(words) == count:
            break
    # keep only the commands that are no substring of another one
    words = [w for w in words if not any(w != v and w in v for v in words)]
    while len(words) < 2:
        words.append("c" * (len(words) + 1) + "d")
    print(len(words))
    print("\n".join(words))


main()
