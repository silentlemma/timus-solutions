import sys


def solve(first, second):
    a = sorted(range(len(first)), key=lambda i: (first[i], i))
    b = sorted(range(len(second)), key=lambda i: (second[i], i))
    if sum(first) > sum(second):
        b.reverse()
    elif sum(first) < sum(second):
        a.reverse()
    return list(zip(a, b))


def run(tokens):
    n = next(tokens)
    first = [next(tokens) for _ in range(n)]
    second = [next(tokens) for _ in range(n)]
    return "".join(f"{a + 1} {b + 1}\n" for a, b in solve(first, second))


if __name__ == "__main__":
    sys.stdout.write(run(iter(map(int, sys.stdin.buffer.read().split()))))
