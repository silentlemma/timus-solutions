"""Users and a tweet from a seed and a mode: mode 1 a few users, 2 the
most users with random followers, 3 the most users in a long chain with
short names, 4 the most users with long names and a long tweet, so
retweets soon get too long, 5 the most users where a short path with
long names competes with a long path with short names, 6 a tweet with
spaces at both ends. Names are distinct, of 1 to 30 Latin letters."""

import random
import string
import sys

MOST = 100
FEW = 6
LONGEST_NAME = 30
LONGEST_TWEET = 140
CHAIN_STEP = 7
SHORT_CHAIN = 4
LETTERS = 3
PREFIX = len("RT @: ")


def make_names(rng, n, low, high):
    names = set()
    while len(names) < n:
        names.add("".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(low, high))))
    out = list(names)
    rng.shuffle(out)
    return out


def tweet(rng, low, high):
    chars = [chr(c) for c in range(32, 128)]
    return "".join(rng.choice(chars) for _ in range(rng.randint(low, high)))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode == 1 else MOST
    if mode == 3:
        names = make_names(rng, n, 1, 2)
    elif mode == 4:
        names = make_names(rng, n, LONGEST_NAME - 2, LONGEST_NAME)
    else:
        names = make_names(rng, n, 1, LONGEST_NAME)
    follow = [set() for _ in range(n)]
    if mode == 3:
        for i in range(n - 1):
            follow[i].add(i + 1)
    elif mode == 5:
        # 0 -> 1 -> T with a long name at 1, and 0 -> a chain of short
        # names -> T; only the chain leaves T a message it can retweet
        names = make_names(rng, n, 2, LETTERS)
        names[1] = "L" * LONGEST_NAME
        chain = list(range(2, 2 + SHORT_CHAIN))
        target = 2 + SHORT_CHAIN
        for k, letter in zip([0] + chain, rng.sample(string.ascii_letters, SHORT_CHAIN + 1)):
            names[k] = letter
        follow[0].update([1, chain[0]])
        follow[1].add(target)
        for a, b in zip(chain, chain[1:] + [target]):
            follow[a].add(b)
        for i in range(target, n - 1):
            follow[i].add(i + 1)
    else:
        chance = rng.choice([0.02, 0.05, 0.2]) if mode != 1 else 0.4
        for a in range(n):
            for b in range(n):
                if a != b and rng.random() < chance:
                    follow[a].add(b)
    if mode == 4:
        text = tweet(rng, LONGEST_TWEET - 2 * LONGEST_NAME, LONGEST_TWEET - LONGEST_NAME)
    elif mode == 6:
        text = "  " + tweet(rng, 1, LONGEST_TWEET - 2 * 2) + "  "
    elif mode == 3:
        text = tweet(rng, 1, CHAIN_STEP)
    elif mode == 5:
        # the chain adds 7 per step over 5 steps, the other way 7 + 36
        short = CHAIN_STEP * (SHORT_CHAIN + 1)
        text = tweet(rng, LONGEST_TWEET - CHAIN_STEP - PREFIX - LONGEST_NAME + 1,
                     LONGEST_TWEET - short)
    else:
        text = tweet(rng, 1, LONGEST_TWEET)
    print(n)
    for i in range(n):
        fs = [names[j] for j in sorted(follow[i])]
        rng.shuffle(fs)
        print(" ".join([names[i], str(len(fs))] + fs))
    print(text)


main()
