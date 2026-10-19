import sys


def solve(x, y, total):
    a = min(x, total)
    b = total - a
    return None if b > y else (a, b)


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    answer = solve(*map(int, tokens))
    if answer is None:
        print("Impossible")
    else:
        print(*answer)


if __name__ == "__main__":
    main()
