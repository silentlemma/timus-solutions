LETTERS = 26


def word(k):
    """The k-th password from 1: by length, then alphabetically, which is
    k written in bijective base 26 with digits a to z."""
    out = []
    while k:
        k, d = divmod(k - 1, LETTERS)
        out.append(chr(ord("a") + d))
    return "".join(reversed(out))


def main():
    n, m = map(int, input().split())
    total = sum(LETTERS**length for length in range(1, n + 1))
    share, extra = divmod(total, m)
    lines = []
    start = 1
    for i in range(m):
        # the first extra processors take one password more
        end = start + share + (1 if i < extra else 0) - 1
        lines.append("%s-%s" % (word(start), word(end)))
        start = end + 1
    print("\n".join(lines))


main()
