"""Two encoded messages: a seed, N and a mode. A random key of N+1 bytes
encodes a clear text of N bytes and the same text after a space. Mode 1
draws the text and key from all bytes, mode 2 takes a text of letters and
spaces, and mode 3 takes key bytes below 16, which print with a leading
zero."""

import random
import sys

SPACE = 0x20
BYTE = 256
SMALL = 16
LETTERS = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 2:
        text = bytes(rng.choice(LETTERS) for _ in range(n))
    else:
        text = bytes(rng.randrange(BYTE) for _ in range(n))
    top = SMALL if mode == 3 else BYTE
    key = bytes(rng.randrange(top) for _ in range(n + 1))
    first = bytes(k ^ c for k, c in zip(key, text))
    second = bytes(k ^ c for k, c in zip(key, bytes([SPACE]) + text))
    sys.stdout.write(first.hex().upper() + "\n" + second.hex().upper() + "\n")


if __name__ == "__main__":
    main()
