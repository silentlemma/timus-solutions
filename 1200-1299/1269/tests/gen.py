"""Words and a text: a seed and a mode. Mode 1 uses a two-letter alphabet
so that words overlap a lot, mode 2 printable characters with spaces,
mode 3 long words and a long text of about 900 KB, mode 4 a text with no
bad word, mode 5 one line of 899 000 letters ending in the bad word,
mode 6 10000 words of ten letters, one of them late in a line. Only
ASCII is used, so positions count bytes and characters alike."""

import random
import sys

TEXT = 900 * 1000
WORDS = 100 * 1000


def random_case(rng, mode):
    if mode == 1:
        alphabet, n, wlen, lines, llen = "ab", rng.randint(1, 30), 6, rng.randint(1, 30), 40
    elif mode == 2:
        alphabet = "".join(chr(c) for c in range(32, 127))
        n, wlen, lines, llen = rng.randint(1, 300), 4, rng.randint(1, 300), 200
    elif mode == 3:
        alphabet, n, wlen, lines, llen = "abc", 9, 10000, 450, 1950
    else:
        alphabet, n, wlen, lines, llen = "abcdefgh", 10000, 9, 4000, 220
    words = []
    for _ in range(n):
        size = rng.randint(1, wlen)
        if mode == 4:
            # every word holds a 'z', which the text never uses
            w = "".join(rng.choice(alphabet) for _ in range(size - 1))
            cut = rng.randint(0, len(w))
            words.append(w[:cut] + "z" + w[cut:])
        else:
            words.append("".join(rng.choice(alphabet) for _ in range(size)))
    assert sum(map(len, words)) <= WORDS
    text = []
    used = 0
    for _ in range(lines):
        size = min(rng.randint(0, llen), TEXT - used)
        used += size + 1
        text.append("".join(rng.choice(alphabet) for _ in range(size)))
    if mode == 3:
        # the longest word appears at the end of the last line
        text[-1] += max(words, key=len)
    return words, text


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        words, text = ["needle", "needlf"], ["e" * 899000 + "needle"]
    elif mode == 6:
        words = ["".join(rng.choice("abcdefghij") for _ in range(10)) for _ in range(9999)]
        words.append("jihgfedcba")
        text = ["k" * 500 + "jihgfedcbajihgf", "x"]
    else:
        words, text = random_case(rng, mode)
    out = [str(len(words))] + words + [str(len(text))] + text
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
