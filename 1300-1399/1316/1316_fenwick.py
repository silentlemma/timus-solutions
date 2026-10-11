import sys

CENTS = 100
DIGITS = 2


def cents(token):
    whole, _, frac = token.partition(b".")
    return int(whole or b"0") * CENTS + int((frac + b"00")[:DIGITS])


def main():
    words = iter(sys.stdin.buffer.read().split())
    ops = []
    for kind in words:
        if kind == b"QUIT":
            break
        price = cents(next(words))
        ops.append((kind, price, int(next(words)) if kind == b"SALE" else 0))
    # prices ranked from the highest down, so that "at least X" is a prefix
    prices = sorted({price for _, price, _ in ops}, reverse=True)
    rank = {price: r + 1 for r, price in enumerate(prices)}
    size = len(prices)
    tree = [0] * (size + 1)
    sold = 0
    for kind, price, k in ops:
        r = rank[price]
        if kind == b"SALE":
            # bids of X or more, a Fenwick prefix sum over the ranks
            count = 0
            while r > 0:
                count += tree[r]
                r &= r - 1
            sold += min(k, count)
        else:
            step = 1 if kind == b"BID" else -1
            while r <= size:
                tree[r] += step
                r += r & -r
    # the exchange earns one cent per piece sold
    print("%d.%02d" % divmod(sold, CENTS))


main()
