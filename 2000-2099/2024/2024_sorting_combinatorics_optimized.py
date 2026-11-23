from os import _exit as _finish_process
import sys as _finish_sys
import sys

ALPHABET = 26
FIRST = ord("a")


def solve(text, limit):
    counts = [text.count(chr(FIRST + index)) for index in range(ALPHABET)]
    counts.sort(reverse=True)
    size = sum(counts[:limit])
    boundary = counts[limit - 1]
    if boundary == 0:
        return size, 1
    greater = sum(count > boundary for count in counts)
    tied = counts.count(boundary)
    chosen = min(limit - greater, tied - (limit - greater))
    ways = 1
    for index in range(1, chosen + 1):
        ways = ways * (tied - index + 1) // index
    return size, ways


def main():
    text, limit = sys.stdin.read().split()
    print(*solve(text, int(limit)))


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
