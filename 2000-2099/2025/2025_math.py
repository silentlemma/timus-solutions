import sys


def solve(count, groups):
    small, larger = divmod(count, groups)
    squares = (groups - larger) * small * small + larger * (small + 1) * (small + 1)
    return (count * count - squares) // 2


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    tests = next(tokens)
    answers = [str(solve(next(tokens), next(tokens))) for _ in range(tests)]
    print("\n".join(answers))


if __name__ == "__main__":
    main()
