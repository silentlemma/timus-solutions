import sys
from math import gcd


def main():
    words = sys.stdin.read().split()
    animals = words[0].split("-")
    parts = []
    for text in words[1:1 + len(animals)]:
        a, b = map(int, text.split("/"))
        g = gcd(a, b)
        parts.append((a // g, b // g))
    # a crossing halves every share, so only shares with a power of two
    # below can come out
    if any(b & (b - 1) for _, b in parts):
        print("No solution")
        return
    # give each animal its share of 2^depth equal leaves, in order, and
    # cross halves of the leaves; a half that is one animal is just that
    # animal
    leaves = max(b for _, b in parts)
    owner = []
    for i, (a, b) in enumerate(parts):
        owner += [i] * (a * (leaves // b))
    rows = []

    def build(lo, hi):
        if owner[lo] == owner[hi - 1]:
            rows.append(animals[owner[lo]])
        else:
            mid = (lo + hi) // 2
            left = build(lo, mid)
            right = build(mid, hi)
            rows.append("%d %d" % (left, right))
        return len(rows)

    build(0, leaves)
    print(len(rows))
    print("\n".join(rows))


main()
