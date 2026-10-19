import sys


def blocks(pos, n, rising):
    # cut the values 1 .. n greedily into runs of consecutive values whose
    # positions alternately rise and fall, the first one as asked
    cuts = []
    v = 1
    while v <= n:
        w = v
        while w < n and (pos[w + 1] > pos[w]) == rising:
            w += 1
        cuts.append((v, w))
        v = w + 1
        rising = not rising
    return cuts


def passes(count):
    # the least k with 2^k >= count
    k = 0
    while (1 << k) < count:
        k += 1
    return k


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, cars = data[0], data[1:1 + data[0]]
    pos = [0] * (n + 1)
    for i, v in enumerate(cars):
        pos[v] = i
    # one pass keeps a chosen set of cars in order and appends the others
    # reversed; over k passes cars end up ordered by their codes of choices
    # in reflected Gray order, reversed once per one in the code
    rising = blocks(pos, n, True)
    falling = blocks(pos, n, False)
    if passes(len(rising)) <= passes(len(falling) + 1):
        runs, first = rising, 0
    else:
        runs, first = falling, 1
    k = passes(len(runs) + first)
    # runs take Gray ranks from first on, so odd ranks are the falling runs
    code = [0] * (n + 1)
    for rank, (lo, hi) in enumerate(runs, first):
        for v in range(lo, hi + 1):
            code[v] = rank ^ (rank >> 1)
    out = [str(k)]
    for bit in range(k):
        kept = [v for v in cars if not code[v] >> bit & 1]
        moved = [v for v in cars if code[v] >> bit & 1]
        cars = kept + moved[::-1]
        out.append(" ".join(map(str, cars)))
    print("\n".join(out))


main()
