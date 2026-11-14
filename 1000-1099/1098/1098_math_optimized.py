import sys


STEP = 1999


def main():
    text = sys.stdin.buffer.read().replace(b"\n", b"").replace(b"\r", b"")
    survivor = 0
    for size in range(2, len(text) + 1):
        survivor = (survivor + STEP) % size

    last = text[survivor : survivor + 1]
    print("Yes" if last == b"?" else "No" if last == b" " else "No comments")


if __name__ == "__main__":
    main()
