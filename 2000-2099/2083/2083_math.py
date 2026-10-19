import sys

SLOT = 10  # bytes per number when packing: sums stay below 2.5 * 10^18 < 2^80
SHORT = 32  # cycles up to this length are summed directly
SPAN = 3  # a product of L and 2L numbers has fewer than 3L


def cyclic(fold, cycle):
    # out[s] = sum over r of fold[r] * cycle[(s + r) mod L]
    size = len(cycle)
    if size <= SHORT:
        return [sum(fold[r] * cycle[(s + r) % size] for r in range(size)) for s in range(size)]
    # one big multiplication: reversed fold times the cycle written twice, with every
    # number in its own SLOT bytes, so the products never overlap
    a = int.from_bytes(b"".join(x.to_bytes(SLOT, "little") for x in reversed(fold)), "little")
    b = int.from_bytes(b"".join(x.to_bytes(SLOT, "little") for x in cycle + cycle), "little")
    product = (a * b).to_bytes(SLOT * (SPAN * size + 1), "little")
    return [int.from_bytes(product[SLOT * k:SLOT * (k + 1)], "little")
            for k in range(size - 1, 2 * size - 1)]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    m, n = data[0], data[1]
    p = [x - 1 for x in data[2:2 + n]]
    q = data[2 + n:2 + n + m]
    # the year t row is p applied t times, so the answer at j is the sum of
    # q_t p^t(j); along a cycle of p this is a cyclic correlation
    answer = [0] * n
    seen = [False] * n
    by_year = [0] + q  # by_year[t] = q_t
    folds = {}  # cycle length -> sums of q_t over t with equal remainders
    for start in range(n):
        if seen[start]:
            continue
        cycle = []
        j = start
        while not seen[j]:
            seen[j] = True
            cycle.append(j)
            j = p[j]
        size = len(cycle)
        if size not in folds:
            folds[size] = [sum(by_year[r::size]) for r in range(size)]
        fold = folds[size]
        values = cyclic(fold, [c + 1 for c in cycle])
        for s, j in enumerate(cycle):
            answer[j] = values[s]
    print(" ".join(map(str, answer)))


main()
