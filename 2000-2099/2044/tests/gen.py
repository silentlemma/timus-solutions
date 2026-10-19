"""Deterministic large strings with dense and sparse palindrome structures."""

import sys

MAX_LENGTH = 300000
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
PERIODS = {
    "uniform": "a",
    "alternating": "ab",
    "cycle26": ALPHABET,
    "period7": "abacaba",
    "period31": "abacabadabacabaeabacabadabacaba",
}
RUN_LENGTHS = (1, 2, 31, 32, 999, 7000, 13, 32000, 31, 64, 17000, 100)
RUN_CYCLE = "abc"
RUN_STEPS = 10000
RUN_MULTIPLIER = 17
RUN_MODULUS = 97


def word_for(mode, n):
    assert 1 <= n <= MAX_LENGTH
    if mode in PERIODS:
        block = PERIODS[mode]
        return (block * ((n + len(block) - 1) // len(block)))[:n]
    if mode == "zimin":
        word = "a"
        for c in ALPHABET[1:]:
            if len(word) >= n:
                break
            word = word + c + word
        return word[:n]
    if mode == "alternating_unique_center":
        half = ("ab" * n)[: n // 2]
        return (half + "c" + half[::-1])[:n]
    if mode == "long_runs_few":
        word = "".join(RUN_CYCLE[i % len(RUN_CYCLE)] * size for i, size in enumerate(RUN_LENGTHS))
        if len(word) < n:
            word += RUN_CYCLE[len(RUN_LENGTHS) % len(RUN_CYCLE)] * (n - len(word))
        return word[:n]
    if mode == "long_runs_many":
        word = "".join(
            RUN_CYCLE[i % len(RUN_CYCLE)] * (1 + (i * RUN_MULTIPLIER) % RUN_MODULUS)
            for i in range(RUN_STEPS)
        )
        assert len(word) >= n
        return word[:n]
    raise ValueError("Unknown string family")


def main():
    print(word_for(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
