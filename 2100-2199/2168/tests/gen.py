import random
import string
import sys


MAX_LENGTH = 100_000
ARGUMENT_COUNT = 3
SMALL_LENGTH = 70
MEDIUM_MIN = 100
MEDIUM_MAX = 4_000
PERIOD_LIMIT = 97
ALPHABET = string.ascii_lowercase
TRAP = "aabaabb"
SHORT_BLOCKS = ("aabaabb", "aabcc", "abacdc", "abcdab", "abcabcab", "abcbde")
REDUCTION_BLOCKS = ("abab", "abcbcabc", "aabaabb")


def random_word(rng, length, alphabet):
    return "".join(rng.choice(alphabet) for _ in range(length))


def small_random(rng):
    length = rng.randint(1, SMALL_LENGTH)
    alphabet_size = rng.randint(1, len(ALPHABET))
    return random_word(rng, length, ALPHABET[:alphabet_size])


def medium_random(rng):
    length = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
    alphabet_size = rng.randint(2, len(ALPHABET))
    return random_word(rng, length, ALPHABET[:alphabet_size])


def maximum_random(rng):
    return random_word(rng, MAX_LENGTH, ALPHABET)


def maximum_binary(rng):
    return random_word(rng, MAX_LENGTH, "ab")


def maximum_unary(rng):
    return rng.choice(ALPHABET) * MAX_LENGTH


def maximum_periodic(rng):
    period_length = rng.randint(2, PERIOD_LIMIT)
    period = random_word(rng, period_length, ALPHABET)
    return (period * (MAX_LENGTH // period_length + 1))[:MAX_LENGTH]


def repeated_unbordered(rng):
    half_length = MAX_LENGTH // 2
    half = "a" + random_word(rng, half_length - 2, "bc") + "d"
    return half + half


def unique_sentinels(rng):
    return "y" + random_word(rng, MAX_LENGTH - 2, "ab") + "z"


def internal_gap(rng):
    left_length = rng.randint(2, MAX_LENGTH - 1 - 2)
    right_length = MAX_LENGTH - left_length - 1
    return "a" * left_length + "z" + "b" * right_length


def greedy_traps(rng):
    alphabet = list(ALPHABET)
    rng.shuffle(alphabet)
    translation = str.maketrans("ab", "".join(alphabet[:2]))
    block = TRAP.translate(translation)
    return (block * (MAX_LENGTH // len(block) + 1))[:MAX_LENGTH]


def long_border_with_tail(rng):
    half_length = (MAX_LENGTH - 2) // 2
    half = "a" + random_word(rng, half_length - 2, "bc") + "d"
    return "y" + half + half + "z"


def alphabet_runs(rng):
    alphabet = list(ALPHABET)
    rng.shuffle(alphabet)
    block_length = MAX_LENGTH // len(alphabet)
    pieces = [char * block_length for char in alphabet]
    pieces[-1] += alphabet[-1] * (MAX_LENGTH - block_length * len(alphabet))
    return "".join(pieces)


def mixed_short_blocks(rng):
    pieces = []
    length = 0
    while length < MAX_LENGTH:
        block = rng.choice(SHORT_BLOCKS)
        pieces.append(block)
        length += len(block)
    return "".join(pieces)[:MAX_LENGTH]


def layered_repetitions(rng):
    word = "a"
    alphabet = list(ALPHABET[1:])
    rng.shuffle(alphabet)
    for separator in alphabet:
        word += separator + word
        if len(word) >= MAX_LENGTH:
            break
    return word[:MAX_LENGTH]


def representative_reductions(rng):
    pieces = []
    length = 0
    while length < MAX_LENGTH:
        alphabet = list(ALPHABET)
        rng.shuffle(alphabet)
        translation = str.maketrans("abc", "".join(alphabet[: len("abc")]))
        block = rng.choice(REDUCTION_BLOCKS).translate(translation)
        pieces.append(block)
        length += len(block)
    return "".join(pieces)[:MAX_LENGTH]


def older_border_with_disruption(rng):
    word_length = (MAX_LENGTH - 2) // 2
    word = "a" + random_word(rng, word_length - 2, "bc") + "d"
    return word + word[:2] + "x" + word[1:]


def maximum_record_history(_rng):
    filler = ALPHABET[-1]
    word = ALPHABET[:-1] + filler * len(ALPHABET)
    for index in range(len(ALPHABET) - 2, -1, -1):
        word += ALPHABET[index] + filler * (index + 1)
    word += ALPHABET[1]
    return word + filler * (MAX_LENGTH - len(word))


GENERATORS = (
    small_random,
    medium_random,
    maximum_random,
    maximum_binary,
    maximum_unary,
    maximum_periodic,
    repeated_unbordered,
    unique_sentinels,
    internal_gap,
    greedy_traps,
    long_border_with_tail,
    alphabet_runs,
    mixed_short_blocks,
    layered_repetitions,
    representative_reductions,
    older_border_with_disruption,
    maximum_record_history,
)


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode = int(sys.argv[1])
    seed = int(sys.argv[2])
    if not 1 <= mode <= len(GENERATORS):
        raise SystemExit("unknown mode")
    word = GENERATORS[mode - 1](random.Random(seed))
    print(len(word))
    print(word)


if __name__ == "__main__":
    main()
