import sys

FORBIDDEN_CHOICES = 3


def count(n):
    if n % 2:
        size = (n - FORBIDDEN_CHOICES) // 2
        return (n * size if size >= 2 else 0), 0
    half = n // 2
    first, second = half - 1, half - 2
    parallel = half * ((first if first >= 2 else 0) + (second if second >= 2 else 0))
    return parallel, half * (n - FORBIDDEN_CHOICES)


if __name__ == "__main__":
    print(*count(int(sys.stdin.buffer.read())))
