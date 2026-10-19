"""Use one constant run and a three-letter tail with no longer palindromes."""

import sys

TAIL = "bcd"


def word_for(n, count, tail):
    if count < min(n, len(TAIL)):
        return "NO"
    if n < len(TAIL):
        return "a" * n
    prefix = count - len(TAIL)
    return "a" * prefix + tail[: n - prefix]


def solve(n):
    tail = (TAIL * ((n + len(TAIL) - 1) // len(TAIL)))[:n]
    for count in range(1, n + 1):
        print(f"{count} : {word_for(n, count, tail)}")


def main():
    solve(int(sys.stdin.buffer.read()))


if __name__ == "__main__":
    main()
