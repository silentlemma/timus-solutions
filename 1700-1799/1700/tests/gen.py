"""One test from a seed and a mode: mode 1 a few objects with a small
vocabulary, mode 2 the most objects and sets with long lines, mode 3
repeated associations and objects without any, mode 4 maximal dense identical
association lists, mode 5 one missing word per object, mode 6 random families
with shared words and a family without the global common word."""

import random
import string
import sys

MOST = 1000
LONGEST = 250


def word(rng, letters):
    return "".join(rng.choice(string.ascii_lowercase[:letters]) for _ in range(rng.randint(1, 3)))


def label(index):
    return "".join(chr(ord("a") + index // (26 ** power) % 26) for power in (2, 1, 0))


def structured(rng, mode):
    vocabulary = [chr(97 + i // 26) + chr(97 + i % 26) for i in range(200)]
    if mode == 5:
        names = list(string.ascii_lowercase)
        print(len(names))
        for name in names:
            words = [other for other in names if other != name]
            rng.shuffle(words)
            print(name + ": " + " ".join(words))
        print(MOST)
        for i in range(MOST):
            # Every additional distinct member removes exactly one word.
            size = 2 + i % 25
            print(" ".join(rng.sample(names, size)))
        return

    names = [label(i) for i in range(MOST)]
    order = list(range(MOST))
    rng.shuffle(order)
    print(MOST)
    for i in order:
        if mode == 4:
            # 3-letter name, ': ', and 82 two-letter words: exactly 250 chars.
            words = vocabulary[:82]
        else:
            family = i % 10
            words = vocabulary[family * 8:family * 8 + 8]
            words += rng.sample(vocabulary[80:], rng.randint(1, 40))
            if family != 9:
                words.append("always")
        rng.shuffle(words)
        print(names[i] + ": " + " ".join(words))
    print(MOST)
    for i in range(MOST):
        if mode == 4:
            group = rng.sample(names, 62)
        else:
            size = rng.randint(2, 60)
            if i % 3 == 0:
                family = rng.randrange(10)
                group = rng.sample(names[family::10], size)
            elif i % 3 == 1:
                group = rng.sample([name for j, name in enumerate(names) if j % 10 != 9], size)
            else:
                group = rng.sample(names, size - 1) + [rng.choice(names[9::10])]
        print(" ".join(group))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (4, 5, 6):
        structured(rng, mode)
        return
    n = rng.randint(2, 8) if mode == 1 else MOST
    m = rng.randint(1, 8) if mode == 1 else MOST
    letters = 6 if mode == 2 else 3
    names = set()
    while len(names) < n:
        names.add("".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(3, 8))))
    names = sorted(names)
    print(n)
    for name in names:
        words = []
        for _ in range(rng.randint(0 if mode == 3 else 1, 60)):
            w = rng.choice(words) if mode == 3 and words and rng.random() < 0.3 else word(rng, letters)
            if len(name) + 2 + len(" ".join(words + [w])) > LONGEST:
                break
            words.append(w)
        print(name + ": " + " ".join(words))
    print(m)
    for _ in range(m):
        group = [rng.choice(names), rng.choice(names)]
        while rng.random() < 0.7:
            pick = rng.choice(names)
            if len(" ".join(group + [pick])) > LONGEST:
                break
            group.append(pick)
        print(" ".join(group))


main()
