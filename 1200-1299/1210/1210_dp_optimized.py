import sys
from math import inf


INPUT_BUFFER = 4096


def numbers():
    # carry only an unfinished token across refills, even when a line is huge.
    pending = b""
    for chunk in iter(lambda: sys.stdin.buffer.read(INPUT_BUFFER), b""):
        data = pending + chunk
        tokens = data.split()
        pending = tokens.pop() if data[-1] > ord(" ") else b""
        for token in tokens:
            if token != b"*":
                yield int(token)
    if pending and pending != b"*":
        yield int(pending)


def main():
    it = numbers()
    levels = int(next(it))
    # the cheapest cost of reaching each planet of the current level
    cost = [0]
    for _ in range(levels):
        nxt = []
        for _ in range(int(next(it))):
            best = inf
            while (src := int(next(it))) != 0:
                price = int(next(it))
                best = min(best, cost[src - 1] + price)
            nxt.append(best)
        cost = nxt
    print(min(cost))


main()
