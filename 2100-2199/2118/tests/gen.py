import random
import string
import sys


ALPHABET = string.ascii_uppercase + string.ascii_lowercase
MAX_SYMBOLS = len(ALPHABET)
MAX_MESSAGE = 10**6
SMALL_SYMBOLS = 8
SMALL_MESSAGE = 12
RANDOM_MESSAGE = 2000
MIN_NON_SINGLE = 3
EXTEND_CHANCE = 4
ARGUMENT_COUNT = 3


def tree_codes(count, depth_limit, rng, min_depth=1, extend=True):
    leaves = [""]
    while len(leaves) < count:
        available = [i for i, code in enumerate(leaves) if len(code) < depth_limit]
        index = rng.choice(available)
        code = leaves.pop(index)
        leaves.extend((code + "0", code + "1"))
    for index, code in enumerate(leaves):
        while len(code) < min_depth:
            code += rng.choice("01")
        if extend and len(code) < depth_limit and rng.randrange(EXTEND_CHANCE) == 0:
            extra = rng.randint(1, depth_limit - len(code))
            code += "".join(rng.choice("01") for _ in range(extra))
        leaves[index] = code
    rng.shuffle(leaves)
    return leaves


def one_single(count, rng):
    other = tree_codes(count - 1, count - 1, rng)
    codes = ["0"] + ["1" + code for code in other]
    rng.shuffle(codes)
    return codes


def random_message(codes, size, rng):
    letters = ALPHABET[: len(codes)]
    return "".join(rng.choice(letters) for _ in range(size))


def make_case(mode, rng):
    if mode == "both-single":
        codes = ["0", "1"]
        size = rng.randint(1, RANDOM_MESSAGE)
        return codes, random_message(codes, size, rng)
    if mode in ("small", "random"):
        limit = SMALL_SYMBOLS if mode == "small" else MAX_SYMBOLS
        message_limit = SMALL_MESSAGE if mode == "small" else RANDOM_MESSAGE
        count = rng.randint(1, limit)
        codes = tree_codes(count, count, rng)
        size = rng.randint(1, message_limit)
        return codes, random_message(codes, size, rng)
    if mode == "no-single":
        count = rng.randint(MIN_NON_SINGLE, MAX_SYMBOLS)
        codes = tree_codes(count, count, rng, min_depth=2)
        size = rng.randint(1, RANDOM_MESSAGE)
        return codes, random_message(codes, size, rng)
    if mode == "one-single":
        count = rng.randint(2, MAX_SYMBOLS)
        codes = one_single(count, rng)
        size = rng.randint(1, RANDOM_MESSAGE)
        return codes, random_message(codes, size, rng)
    if mode == "max-random":
        codes = tree_codes(MAX_SYMBOLS, MAX_SYMBOLS, rng)
        return codes, random_message(codes, MAX_MESSAGE, rng)
    if mode in ("max-repeated", "max-alternating"):
        codes = one_single(MAX_SYMBOLS, rng)
        indices = sorted(range(MAX_SYMBOLS), key=lambda index: len(codes[index]))
        longest = ALPHABET[indices[-1]]
        if mode == "max-repeated":
            return codes, longest * MAX_MESSAGE
        shortest = ALPHABET[indices[0]]
        return codes, (shortest + longest) * (MAX_MESSAGE // 2)
    if mode == "max-long-code":
        width = MAX_SYMBOLS - 1
        codes = ["0" + format(index, f"0{width}b") for index in range(MAX_SYMBOLS)]
        return codes, ALPHABET[-1] * MAX_MESSAGE
    if mode == "max-sync":
        codes = ["1" * index + "0" for index in range(MAX_SYMBOLS)]
        return codes, ALPHABET[-1] * MAX_MESSAGE
    if mode == "max-delayed":
        codes = ["0"] + ["1" * index + "0" for index in range(1, MAX_SYMBOLS - 1)]
        codes.append("1" * MAX_SYMBOLS)
        return codes, ALPHABET[-1] + ALPHABET[0] * (MAX_MESSAGE - 1)
    if mode == "max-cycle":
        codes = ["1" * index + "0" for index in range(MAX_SYMBOLS)]
        message = (ALPHABET * (MAX_MESSAGE // MAX_SYMBOLS + 1))[:MAX_MESSAGE]
        return codes, message
    if mode == "max-incomplete":
        codes = ["0"] + ["1" * index + "0" for index in range(2, MAX_SYMBOLS)]
        codes.append("1" * MAX_SYMBOLS)
        repeated = ALPHABET[-2] * (MAX_MESSAGE - 1)
        return codes, repeated + ALPHABET[-1]
    raise SystemExit("unknown mode")


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    codes, message = make_case(mode, rng)
    if rng.randrange(2):
        codes = [code.translate(str.maketrans("01", "10")) for code in codes]
    print(len(codes))
    print(message)
    print("\n".join(codes))


if __name__ == "__main__":
    main()
