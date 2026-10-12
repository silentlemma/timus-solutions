"""Blogs: a seed and a mode. Mode 1 gives 100 bloggers mentioning one
another at random in long blogs, mode 2 mentions of people without a
blog, of oneself and of the same friend many times, mode 3 friend tags
with spaces and other tags inside and blogs on a single line. Mode 4
fills all 100 blogs with 1000 lines of 255 characters, mode 5 makes a
complete mutual graph, mode 6 makes a directed ring with boundary-length
lines and outsiders, mode 7 makes small random blogs with multiline
friend contents and names interrupted by formatting tags."""

import random
import string
import sys

N = 100
LINES = 300
MAX_LINES = 1000
MAX_WIDTH = 255
WORDS = ["the", "net", "today", "Hello", "world", "link", "blog", "post", "x1", "?", "!", ","]
NAME = string.ascii_letters + "_"


def extra_mode(seed, mode):
    sys.stdout.reconfigure(newline="\n")
    rng = random.Random(seed)
    names = ["User_" + chr(65 + i // 26) + chr(65 + i % 26) for i in range(N)]
    rng.shuffle(names)
    if mode == 7:
        names = rng.sample(["A", "AA", "Aa", "B", "Z", "_", "_a", "a", "aa"], 8)
    print(len(names))
    for index, name in enumerate(names):
        print(name)
        if mode == 4:
            print("<blog>" + "x" * (MAX_WIDTH - len("<blog>")))
            for _ in range(MAX_LINES - 2):
                print("x" * MAX_WIDTH)
            tail = "<friend>" + names[(index + 1) % N] + "</friend></blog>"
            print("x" * (MAX_WIDTH - len(tail)) + tail)
        elif mode == 5:
            print("<blog>")
            targets = names[:]
            rng.shuffle(targets)
            for target in targets:
                print("<friend>" + target + "</friend>")
            print("</blog>")
        elif mode == 6:
            print("<blog>")
            for target in [
                names[(index + 1) % N], "Outside", name, names[(index + 1) % N]
            ]:
                tag = "<friend>" + target + "</friend>"
                print(tag + " " * (MAX_WIDTH - len(tag)))
            print("</blog>")
        else:
            print("<blog>")
            for _ in range(rng.randint(0, 12)):
                target = rng.choice(names + ["Ghost", "Phantom"])
                middle = rng.randrange(len(target) + 1)
                print(
                    "<friend>\n " + target[:middle] + "<b>" + target[middle:]
                    + "</b>\n</friend>"
                )
            print("</blog>")


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    if mode in (4, 5, 6, 7):
        extra_mode(seed, mode)
        return
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
