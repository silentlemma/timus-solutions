import sys


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n = next(tok)
    segs = [(next(tok), next(tok)) for _ in range(n)]
    # the segment that ends first leaves the most room for the rest; touching
    # ends share no inner point
    chosen = []
    end = None
    for a, b in sorted(segs, key=lambda s: s[1]):
        if end is None or a >= end:
            chosen.append((a, b))
            end = b
    print(len(chosen))
    print("\n".join("%d %d" % s for s in chosen))


main()
