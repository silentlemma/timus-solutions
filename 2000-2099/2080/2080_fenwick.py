import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    uses = [0] + [int(v) for v in data[2:2 + k]]  # uses[1..k]
    # the stack is kept in order of next use: after a card is used, the cards above
    # it are those used before its next use, the distinct cards in between
    nxt = [k + 1] * (k + 2)
    seen = [k + 1] * (n + 1)
    for i in range(k, 0, -1):
        nxt[i] = seen[uses[i]]
        seen[uses[i]] = i
    # Fenwick tree over moments: a moment j counts once the query time i reaches
    # the previous use of its card, so the counted moments are first uses after i
    tree = [0] * (k + 2)

    def add(j):
        while j <= k:
            tree[j] += 1
            j += j & -j

    def prefix(j):
        s = 0
        while j > 0:
            s += tree[j]
            j -= j & -j
        return s

    for card in range(1, n + 1):
        if seen[card] <= k:
            add(seen[card])
    out = []
    for i in range(1, k + 1):
        if nxt[i] <= k:
            add(nxt[i])
        out.append(prefix(nxt[i] - 1) - prefix(i))
    first = sorted(range(1, n + 1), key=lambda card: seen[card])
    sys.stdout.write(" ".join(map(str, first)) + "\n" + "\n".join(map(str, out)) + "\n")


main()
