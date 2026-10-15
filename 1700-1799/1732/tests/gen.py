"""One test from a seed and a mode: mode 1 a short saying over two
letters and a target taken from it or made up, mode 2 a long random
saying and a target cut out of it, mode 3 one long word of a's and a
target that almost fits it, the worst case for naive searching, mode 4
a long saying with a target that fails at the very end, mode 5 many
one-letter words."""

import random
import sys

LONGEST = 100000
SHORT = 12
WORD = 8


def saying(rng, size, alphabet):
    words, total = [], 0
    while True:
        w = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, WORD)))
        if total + len(w) + 1 > size and words:
            return " ".join(words)
        words.append(w)
        total += len(w) + 1


def cut(rng, text):
    # erase random letters and keep the rest as the target
    kept = "".join(c if c == " " or rng.random() < 0.6 else " " for c in text)
    target = " ".join(kept.split())
    return target or text[0]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        text = saying(rng, rng.randint(1, SHORT), "ab")
        target = cut(rng, text) if rng.random() < 0.5 else saying(rng, rng.randint(1, SHORT), "ab")
    elif mode == 2:
        text = saying(rng, LONGEST, "abc")
        target = cut(rng, text)
    elif mode == 3:
        text = "a" * LONGEST
        target = "a" * (LONGEST // 2 - 1) + "b"
    elif mode == 4:
        text = saying(rng, LONGEST - 2 * WORD - 1, "ab")
        target = cut(rng, text) + " " + "b" * WORD * 2
    else:
        text = " ".join(rng.choice("ab") for _ in range(LONGEST // 2))
        target = cut(rng, text)
    if target == text:
        target = target[:-1] if len(target) > 1 and target[-2] != " " else target + "a"
    print(text)
    print(target.strip() or "a")


main()
