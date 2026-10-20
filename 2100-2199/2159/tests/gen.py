import random
import sys


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
WORD_WIDTH = 4
MAX_COUNT = 100000
MAX_TOTAL = 2000000
SMALL_MIN = 3
SMALL_WORDS = 50
SMALL_RULES = 200
DAG_WORDS = 400
DAG_RULES = 1500
PREFIX_RULES = 2000
ARGUMENT_COUNT = 3


def word(index):
    letters = []
    for _ in range(WORD_WIDTH):
        index, digit = divmod(index, len(ALPHABET))
        letters.append(ALPHABET[digit])
    assert index == 0
    return "".join(reversed(letters))


def small(rng):
    count = rng.randint(1, SMALL_WORDS)
    words = [word(index) for index in range(count)]
    if count >= SMALL_MIN:
        words[:SMALL_MIN] = ["a", "aa", "aaa"]
    rng.shuffle(words)
    keywords = rng.sample(words, rng.randint(1, count))
    rule_count = rng.randint(1, min(SMALL_RULES, count * count))
    indices = rng.sample(range(count * count), rule_count)
    rules = [(words[index // count], words[index % count]) for index in indices]
    return keywords, rules


def dag(rng):
    count = rng.randint(SMALL_MIN, DAG_WORDS)
    words = [word(index) for index in range(count)]
    rng.shuffle(words)
    keywords = rng.sample(words, rng.randint(1, count))
    possible = [(left, right) for left in range(count) for right in range(left + 1, count)]
    rule_count = rng.randint(1, min(DAG_RULES, len(possible)))
    rules = [(words[left], words[right]) for left, right in rng.sample(possible, rule_count)]
    return keywords, rules


def chain(rng, cyclic=False):
    count = MAX_COUNT if cyclic else MAX_COUNT + 1
    words = [word(index) for index in range(count)]
    rng.shuffle(words)
    rules = list(zip(words, words[1:]))
    if cyclic:
        rules.append((words[-1], words[0]))
    rng.shuffle(rules)
    return [words[0]], rules


def heap(rng):
    root = "z"
    rules = [(root, word(index)) for index in range(MAX_COUNT)]
    rng.shuffle(rules)
    return [root], rules


def maximum(rng):
    words = [word(index) for index in range(MAX_COUNT * 2)]
    rng.shuffle(words)
    keywords = words[:MAX_COUNT]
    rules = list(zip(keywords, words[MAX_COUNT:]))
    rng.shuffle(keywords)
    rng.shuffle(rules)
    return keywords, rules


def distinct(rng):
    keywords = [word(index) for index in range(MAX_COUNT)]
    rules = [
        (word(MAX_COUNT + index * 2), word(MAX_COUNT + index * 2 + 1))
        for index in range(MAX_COUNT)
    ]
    rng.shuffle(keywords)
    rng.shuffle(rules)
    return keywords, rules


def budget(rng):
    letter = rng.choice(ALPHABET)
    return [letter * (MAX_TOTAL - 2)], [("a", "b")]


def prefix(rng):
    root = "z"
    target_total = MAX_TOTAL - PREFIX_RULES - 1
    length, extra = divmod(target_total, PREFIX_RULES)
    targets = [
        "a" * (length - WORD_WIDTH + (index < extra)) + word(index)
        for index in range(PREFIX_RULES)
    ]
    rules = [(root, target) for target in targets]
    rng.shuffle(rules)
    return [root], rules


def irrelevant(rng):
    keywords = [word(index) for index in range(MAX_COUNT)]
    cycle = [word(MAX_COUNT + index) for index in range(MAX_COUNT)]
    rules = list(zip(cycle, cycle[1:] + cycle[:1]))
    rng.shuffle(keywords)
    rng.shuffle(rules)
    return keywords, rules


def emit(keywords, rules):
    assert 1 <= len(keywords) <= MAX_COUNT
    assert 1 <= len(rules) <= MAX_COUNT
    assert len(set(keywords)) == len(keywords)
    assert len(set(rules)) == len(rules)
    total = sum(map(len, keywords)) + sum(len(left) + len(right) for left, right in rules)
    assert total <= MAX_TOTAL
    lines = [f"{len(keywords)} {len(rules)}"]
    lines.extend(keywords)
    lines.extend(f"{left} {right}" for left, right in rules)
    sys.stdout.write("\n".join(lines) + "\n")


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode = sys.argv[1]
    rng = random.Random(int(sys.argv[2]))
    modes = {
        "small": small,
        "dag": dag,
        "chain": chain,
        "heap": heap,
        "max": maximum,
        "words": distinct,
        "budget": budget,
        "prefix": prefix,
        "cycle": lambda source: chain(source, cyclic=True),
        "irrelevant": irrelevant,
    }
    if mode not in modes:
        raise SystemExit("unknown mode: " + mode)
    emit(*modes[mode](rng))


if __name__ == "__main__":
    main()
