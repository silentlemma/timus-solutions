"""Generate large n inputs, or reproduce the exhaustive certificate with --proof.

Modes phase_0..phase_5 use 1993..1998 with matching residue modulo six;
near_max uses 1999 and maximum uses 2000. The integer seed is accepted."""

from itertools import product


def palindromes(word):
    return {
        word[left:right]
        for left in range(len(word))
        for right in range(left + 1, len(word) + 1)
        if word[left:right] == word[left:right][::-1]
    }


def certificate():
    histograms = {}
    for n in range(1, 10):
        histogram = {}
        for bits in product("ab", repeat=n):
            count = len(palindromes("".join(bits)))
            histogram[count] = histogram.get(count, 0) + 1
        expected = {n: 2**n} if n <= 7 else {7: 4, 8: 252} if n == 8 else {8: 24, 9: 488}
        assert histogram == expected, (n, histogram)
        histograms[n] = histogram
    period = "aababb"
    windows = {}
    for size in range(1, 7):
        words = {(period * 3)[start : start + size] for start in range(len(period))}
        windows[size] = sorted(word for word in words if word == word[::-1])
    assert not windows[5] and not windows[6]
    assert {word for group in windows.values() for word in group} == {
        "a",
        "b",
        "aa",
        "bb",
        "aba",
        "bab",
        "abba",
        "baab",
    }
    return histograms, windows


import sys


def main():
    if sys.argv[1:] == ["--proof"]:
        for n, histogram in certificate()[0].items():
            print(n, sorted(histogram.items()))
        return
    int(sys.argv[1])
    modes = {f"phase_{n % 6}": n for n in range(1993, 1999)}
    modes.update(near_max=1999, maximum=2000)
    print(modes[sys.argv[2]])


if __name__ == "__main__":
    main()
