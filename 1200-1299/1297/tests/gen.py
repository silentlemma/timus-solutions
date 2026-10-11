"""One line of Latin letters: a seed and a mode. Mode 1 uses the letters
a and b, mode 2 any letters of both cases, mode 3 1000 copies of one
letter, mode 4 a long palindrome hidden in random letters."""

import random
import string
import sys

LENGTH = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        s = "".join(rng.choice("ab") for _ in range(rng.randint(1, LENGTH)))
    elif mode == 2:
        s = "".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, LENGTH)))
    elif mode == 3:
        s = rng.choice(string.ascii_letters) * LENGTH
    else:
        half = "".join(rng.choice("xyz") for _ in range(rng.randint(1, LENGTH // 4)))
        core = half + rng.choice(["", "q"]) + half[::-1]
        left = rng.randint(0, LENGTH - len(core))
        noise = [rng.choice(string.ascii_uppercase) for _ in range(LENGTH - len(core))]
        s = "".join(noise[:left]) + core + "".join(noise[left:])
    print(s)


main()
