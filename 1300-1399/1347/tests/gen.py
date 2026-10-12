"""Blogs: a seed and a mode. Mode 1 gives 100 bloggers mentioning one
another at random in long blogs, mode 2 mentions of people without a
blog, of oneself and of the same friend many times, mode 3 friend tags
with spaces and other tags inside and blogs on a single line."""

import random
import string
import sys

N = 100
LINES = 300
WORDS = ["the", "net", "today", "Hello", "world", "link", "blog", "post", "x1", "?", "!", ","]
NAME = string.ascii_letters + "_"


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    names = set()
    while len(names) < N:
        names.add("".join(rng.choice(NAME) for _ in range(rng.randint(1, 12))))
    names = sorted(names)
    rng.shuffle(names)
    outsiders = ["Ghost_" + str(i) for i in range(10)] if mode == 2 else []
    print(N)
    for name in names:
        print(name)
        lines = []
        for _ in range(rng.randint(1, LINES)):
            words = []
            for _ in range(rng.randint(0, 12)):
                if rng.random() < 0.05:
                    friend = rng.choice(names + outsiders + ([name] if mode == 2 else []))
                    if mode == 3:
                        friend = (
                            rng.choice([" ", ""]) + "<b>" + friend + "</b>" + rng.choice([" ", ""])
                        )
                    words.append("<friend>" + friend + "</friend>")
                else:
                    words.append(rng.choice(WORDS))
            lines.append(" ".join(words))
        if mode == 3 and rng.random() < 0.3:
            print("<blog>" + " ".join(lines[:3]) + "</blog>")
        else:
            print("<blog>")
            print("\n".join(lines))
            print("</blog>")


main()
