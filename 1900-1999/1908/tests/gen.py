from itertools import product
import random
import sys

MAX_TOTAL = 100000
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def main():
    randomizer = random.Random(int(sys.argv[1]))
    mode = int(sys.argv[2])
    if mode == 1:
        words = [""]
        for _ in range(randomizer.randint(1, 7)):
            parent = randomizer.choice(words)
            words.remove(parent)
            width = randomizer.randint(1, min(3, 9 - len(words)))
            words.extend(parent + letter for letter in ALPHABET[:width])
    elif mode == 2:
        words = ["a" * MAX_TOTAL]
    elif mode == 3:
        stem = "a" * (MAX_TOTAL // 2 - 1)
        words = [stem + "b", stem + "c"]
    elif mode == 4:
        words = list(ALPHABET)
    elif mode == 5:
        words = ["".join(letters) for letters in product("ab", repeat=12)]
    elif mode == 6:
        words = ["".join(letters) for letters in product(ALPHABET, repeat=3)]
    elif mode == 7:
        tail = "a" * (MAX_TOTAL // len(ALPHABET) - 1)
        words = [letter + tail for letter in ALPHABET]
    elif mode == 8:
        stem = "a" * (MAX_TOTAL // len(ALPHABET) - 1)
        words = [stem + letter for letter in ALPHABET]
    elif mode == 9:
        values = set()
        while len(values) < 10000:
            values.add("".join(randomizer.choices(ALPHABET[:8], k=8)))
        words = sorted(values)
    elif mode == 10:
        words = [""]
        total = 0
        for _ in range(8000):
            index = randomizer.randrange(len(words))
            parent = words[index]
            width = randomizer.randint(2, 5)
            added = (width - 1) * len(parent) + width
            if total + added > MAX_TOTAL:
                break
            total += added
            words[index] = words[-1]
            words.pop()
            words.extend(parent + letter for letter in ALPHABET[:width])
    elif mode == 11:
        suffixes = ["aa", "ab", "ac", "ad", "bxa", "bxb"]
        stem = "z" * ((MAX_TOTAL - sum(map(len, suffixes))) // len(suffixes))
        words = [stem + suffix for suffix in suffixes]
    else:
        depth = 445
        words = ["a" * index + "b" for index in range(depth)] + ["a" * depth]
    randomizer.shuffle(words)
    assert words and all(words) and sum(map(len, words)) <= MAX_TOTAL
    ordered = sorted(words)
    assert all(not right.startswith(left) for left, right in zip(ordered, ordered[1:]))
    print(len(words))
    print("\n".join(words))


if __name__ == "__main__":
    main()
