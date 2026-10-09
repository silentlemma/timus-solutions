import sys

STEP = 1999


def main():
    data = sys.stdin.buffer.read()
    n = sum(1 for c in data if c not in b"\r\n")
    # Josephus: with m characters left, the one that stays last sits at
    # (survivor of m - 1) + STEP, counted from where the first deletion was
    survivor = 0
    for m in range(2, n + 1):
        survivor = (survivor + STEP) % m
    last = bytes(c for c in data if c not in b"\r\n")[survivor : survivor + 1]
    print("Yes" if last == b"?" else "No" if last == b" " else "No comments")


main()
