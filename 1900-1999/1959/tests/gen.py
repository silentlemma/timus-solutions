import sys


SYMBOL_LIMIT = 100000
BLOCK_WIDTH = 17
BLOCK_ALPHABET = 1000


def main():
    kind, size = sys.argv[1], int(sys.argv[2])
    unique = list(range(1, size + 1))
    zeros = [0] * size
    if kind == "unknown_text_unique":
        text, pattern = zeros, unique[: size // 2]
    elif kind == "unknown_pattern_unique":
        text, pattern = unique, [0] * (size // 2)
    elif kind == "unknown_text_constant":
        text, pattern = zeros, [SYMBOL_LIMIT] * (size // 2)
    elif kind == "unknown_pattern_one":
        text, pattern = [SYMBOL_LIMIT] * size, [0]
    elif kind == "unknown_pattern_long":
        text, pattern = unique, [0] * (size - 1)
    elif kind == "unknown_text_one":
        text, pattern = zeros, [SYMBOL_LIMIT]
    elif kind == "intact_long":
        text, pattern = unique, unique[:-1]
    else:
        assert kind == "unknown_pattern_blocks"
        text = [(i // BLOCK_WIDTH) % BLOCK_ALPHABET + 1 for i in range(size)]
        pattern = [0] * (size // 2)
    print(len(text))
    print(*text)
    print(len(pattern))
    print(*pattern)


if __name__ == "__main__":
    main()
