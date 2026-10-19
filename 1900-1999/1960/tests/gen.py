import random
import sys


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
RUN_LENGTH = 4000
SIZE_LIMIT = 100000


def main():
    kind, size, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    assert 1 <= size <= SIZE_LIMIT
    if kind == "unary":
        text = "a" * size
    elif kind == "alternating":
        text = ("ab" * ((size + 1) // 2))[:size]
    elif kind == "alphabet_cycle":
        text = (ALPHABET * ((size + len(ALPHABET) - 1) // len(ALPHABET)))[:size]
    elif kind == "ruler":
        text = "".join(
            chr(ord("a") + (i & -i).bit_length() - 1) for i in range(1, size + 1)
        )
    elif kind == "long_jump":
        text = "a" * (size // 2) + "b" + "a" * (size - size // 2 - 1)
    elif kind == "fresh_runs":
        text = "".join(chr(ord("a") + i // RUN_LENGTH) for i in range(size))
    else:
        rng = random.Random(seed)
        if kind == "random_3":
            for _ in range(size):
                rng.choice(ALPHABET)
            alphabet = "abc"
        else:
            assert kind == "random_26"
            alphabet = ALPHABET
        text = "".join(rng.choice(alphabet) for _ in range(size))
    print(text)


if __name__ == "__main__":
    main()
