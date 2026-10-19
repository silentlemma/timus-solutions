"""Generate palindrome-count comparisons: gen.py seed mode.

Modes: equal_unary, disjoint_unary, equal_alternating, aggregate_unary,
many_single_letters, aggregate_period2, aggregate_disjoint_period2,
aggregate_period26, many_varied_single_letters, max_ruler, max_binary, max_letters.
Single maximum pairs have length 200000; aggregate pairs have length 199998.
Tiny batches contain 1999998 pairs and exactly 8000000 input bytes.
The seed affects max_binary and max_letters; other modes are deterministic.
"""

import random
import sys

MAX_WORD_LENGTH = 200000
AGGREGATE_WORD_LENGTH = 199998
AGGREGATE_CASES = 20
TINY_CASES = 1999998
REPEAT_CHUNK = 1024


def parts(seed, mode):
    if mode in ("many_single_letters", "many_varied_single_letters"):
        yield str(TINY_CASES) + "\n"
        block = "a\na\n" if mode == "many_single_letters" else "c\nc\na\nb\n"
        repeats = TINY_CASES if mode == "many_single_letters" else TINY_CASES // 2
        while repeats >= REPEAT_CHUNK:
            yield block * REPEAT_CHUNK
            repeats -= REPEAT_CHUNK
        yield block * repeats
        return
    n = MAX_WORD_LENGTH
    count = 1
    if mode.startswith("aggregate_"):
        n, count = AGGREGATE_WORD_LENGTH, AGGREGATE_CASES
    if mode in ("equal_unary", "aggregate_unary"):
        a = b = "a" * n
    elif mode == "disjoint_unary":
        a, b = "a" * n, "b" * n
    elif mode in ("equal_alternating", "aggregate_period2"):
        a, b = "ab" * (n // 2), "ba" * (n // 2)
    elif mode == "aggregate_disjoint_period2":
        a, b = "ab" * (n // 2), "cd" * (n // 2)
    elif mode == "aggregate_period26":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        a = b = (alphabet * ((n + len(alphabet) - 1) // len(alphabet)))[:n]
    elif mode == "max_ruler":
        a = "".join(chr(ord("a") + (i & -i).bit_length() - 1) for i in range(1, n + 1))
        b = a[1:] + a[:1]
    elif mode in ("max_binary", "max_letters"):
        rng = random.Random(seed)
        alphabet = "ab" if mode == "max_binary" else "abcdefghijklmnopqrstuvwxyz"
        a = "".join(rng.choice(alphabet) for _ in range(n))
        b = "".join(rng.choice(alphabet) for _ in range(n))
    else:
        raise ValueError("Unknown generation mode")
    yield str(count) + "\n"
    for _ in range(count):
        yield a + "\n" + b + "\n"


def main():
    for piece in parts(int(sys.argv[1]), sys.argv[2]):
        sys.stdout.write(piece)


if __name__ == "__main__":
    main()
