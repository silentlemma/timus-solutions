import sys

STEP = 1999


def main():
    data = sys.stdin.buffer.read()
    n = sum(1 for c in data if c not in b"\r\n")
    # Josephus: J(m) is zero-based from the original counting start.
    # After the first deletion, counting restarts STEP positions from that start.
    # Thus J(m) = (J(m - 1) + STEP) % m, with J(1) = 0.
    survivor = 0
    for m in range(2, n + 1):
        survivor = (survivor + STEP) % m
    last = bytes(c for c in data if c not in b"\r\n")[survivor : survivor + 1]
    print("Yes" if last == b"?" else "No" if last == b" " else "No comments")


main()
