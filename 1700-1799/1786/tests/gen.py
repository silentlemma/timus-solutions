"""One test from a seed and a mode: mode 1 random letters of any case,
mode 2 random letters with a few damaged copies of Sandro planted in
them, mode 3 the letters of Sandro in all cases."""

import random
import string
import sys

NAME = "Sandro"
LIMIT = 200
DAMAGE = 3


def damaged(rng):
    word = list(NAME)
    for _ in range(rng.randint(0, DAMAGE)):
        k = rng.randrange(len(word))
        word[k] = rng.choice([word[k].swapcase(), rng.choice(string.ascii_letters)])
    return "".join(word)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    length = rng.randint(len(NAME), LIMIT)
    if mode == 3:
        letters = NAME + NAME.upper() + NAME.lower()
        text = "".join(rng.choice(letters) for _ in range(length))
    else:
        text = [rng.choice(string.ascii_letters) for _ in range(length)]
        if mode == 2:
            for _ in range(rng.randint(1, DAMAGE)):
                start = rng.randint(0, length - len(NAME))
                text[start:start + len(NAME)] = damaged(rng)
        text = "".join(text)
    print(text)


main()
