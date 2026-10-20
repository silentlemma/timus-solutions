import sys


def blue_wins(n, r1, c1, r2, c2):
    # Reflect the board so Blue starts to the left of Red.
    if c1 > c2:
        c1, c2 = n + 1 - c1, n + 1 - c2
    gap = c2 - c1
    left, right = c1 - 1, n - c2
    if r1 == r2:
        return left > right or (left == right and gap % 2 == 0)
    if gap == 0 or left == right:
        return False
    if gap == 1:
        return True
    # A one-column tail advantage makes the gap parity decisive.
    if left == right + 1 or right == left + 1:
        return gap % 2 == 1
    return left > right


def main():
    n, r1, c1, r2, c2 = map(int, sys.stdin.buffer.read().split())
    print("Blue" if blue_wins(n, r1, c1, r2, c2) else "Red")


if __name__ == "__main__":
    main()
