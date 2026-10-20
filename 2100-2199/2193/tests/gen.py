import random
import string
import sys


MAX_WORDS = 100_000
MAX_QUERIES = 100_000
MAX_LENGTH = 100_000
MAX_TOTAL = 1_000_000
SMALL_WORDS = 8
SMALL_LENGTH = 24
SMALL_QUERIES = 48
MEDIUM_WORDS = 1_000
PAIR_WORDS = 448
SHORT_LENGTH = MAX_TOTAL // MAX_WORDS
MEDIUM_LENGTH = MAX_TOTAL // MEDIUM_WORDS
LONG_WORDS = MAX_TOTAL // MAX_LENGTH
NEAR_CHANGES = 80
CLUSTER_WIDTH = 32
USEFUL_MISMATCHES = 17
ALPHABET = string.ascii_lowercase


def random_word(rng, length):
    return "".join(rng.choices(ALPHABET, k=length))


def make_words(mode, rng):
    if mode == "small":
        words = []
        for _ in range(rng.randint(2, SMALL_WORDS)):
            if words and rng.randrange(2):
                word = list(rng.choice(words))
                word[rng.randrange(len(word))] = rng.choice(ALPHABET)
                words.append("".join(word))
            else:
                words.append(random_word(rng, rng.randint(1, SMALL_LENGTH)))
        return words
    if mode == "max_words":
        return [random_word(rng, SHORT_LENGTH) for _ in range(MAX_WORDS)]
    if mode == "max_total":
        return [random_word(rng, MEDIUM_LENGTH) for _ in range(MEDIUM_WORDS)]
    if mode == "max_pairs":
        length = MAX_TOTAL // PAIR_WORDS
        positions = rng.sample(range(length), PAIR_WORDS)
        base = "a" * length
        return [base[:position] + "b" + base[position + 1 :] for position in positions]
    if mode == "equal":
        return ["a" * MAX_LENGTH for _ in range(LONG_WORDS)]
    if mode == "different":
        return [letter * MAX_LENGTH for letter in ALPHABET[:LONG_WORDS]]
    if mode == "cutoff":
        words = ["a" * MAX_LENGTH]
        for index in range(1, LONG_WORDS):
            changes = USEFUL_MISMATCHES + index % 2
            words.append("a" * (MAX_LENGTH - changes) + "b" * changes)
        return words
    if mode in ("near", "clusters", "trim"):
        base = random_word(rng, MAX_LENGTH) if mode == "near" else "a" * MAX_LENGTH
        words = [base]
        for _ in range(1, LONG_WORDS):
            word = list(base)
            if mode == "near":
                positions = rng.sample(range(MAX_LENGTH), NEAR_CHANGES)
            else:
                centers = (0, MAX_LENGTH // 2, MAX_LENGTH - CLUSTER_WIDTH)
                positions = [
                    center + offset for center in centers for offset in range(CLUSTER_WIDTH)
                ]
            for position in positions:
                word[position] = rng.choice(ALPHABET[1:])
            words.append("".join(word))
        return words
    raise ValueError("unknown mode: " + mode)


def generate(mode, seed):
    rng = random.Random(seed)
    words = make_words(mode, rng)
    query_count = rng.randint(1, SMALL_QUERIES) if mode == "small" else MAX_QUERIES
    lines = [str(len(words)) + " " + str(query_count), *words]
    pairs = []
    if mode == "max_pairs":
        pairs = [(first, second) for second in range(1, len(words)) for first in range(second)]
        rng.shuffle(pairs)
    for index in range(query_count):
        if pairs:
            first, second = pairs[index]
        else:
            first = rng.randrange(len(words))
            second = rng.randrange(len(words))
        limit = min(len(words[first]), len(words[second]))
        if mode == "cutoff":
            first = 0
            second = 1 + index % (len(words) - 1)
            cut = 0 if index % 2 else rng.randrange(USEFUL_MISMATCHES + 2)
        elif mode == "trim":
            cuts = (0, 1, CLUSTER_WIDTH - 1, CLUSTER_WIDTH, limit // 2, limit - 1)
            cut = cuts[index % len(cuts)]
        elif index % 2:
            cut = rng.randrange(limit)
        else:
            cut = 0 if rng.randrange(2) else limit - 1
        lines.append(f"{first + 1} {second + 1} {cut}")
    sys.stdout.write("\n".join(lines) + "\n")


def main():
    if len(sys.argv) != 1 + 2:
        raise SystemExit("usage: python gen.py MODE SEED")
    generate(sys.argv[1], int(sys.argv[2]))


if __name__ == "__main__":
    main()
