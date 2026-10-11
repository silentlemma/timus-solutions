import sys


def longest(text, letter, top):
    """The longest run of letter in text, by binary search on its length."""
    lo, hi = 0, top
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if text.find(letter * mid) >= 0:
            lo = mid
        else:
            hi = mid - 1
    return lo


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rows = data[1 : n + 1]
    # every line of cells as one string: rows, columns and both diagonals,
    # the diagonals being the columns of the rows shifted step by step
    pad = b"."
    lines = list(rows) + [bytes(c) for c in zip(*rows)]
    lines += [bytes(c) for c in zip(*(pad * i + r + pad * (n - 1 - i) for i, r in enumerate(rows)))]
    lines += [bytes(c) for c in zip(*(pad * (n - 1 - i) + r + pad * i for i, r in enumerate(rows)))]
    text = pad.join(lines)
    small, large = longest(text, b"s", n), longest(text, b"S", n)
    print("s" if small > large else "S" if large > small else "?")
    print(max(small, large))


main()
