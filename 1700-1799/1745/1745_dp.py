import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    words = data[1:n + 1]
    # each word: (net change of the depth, lowest depth reached, length)
    info = []
    for w in words:
        depth = low = 0
        for c in w:
            depth += 1 if c == "(" else -1
            low = min(low, depth)
        info.append((depth, low, len(w)))
    # in a best answer the words that open more than they close come first,
    # those that dip least first; the rest go last, those that end highest
    # above their lowest point first
    rising = sorted((i for i in range(n) if info[i][0] >= 0), key=lambda i: -info[i][1])
    falling = sorted((i for i in range(n) if info[i][0] < 0),
                     key=lambda i: info[i][1] - info[i][0])
    order = rising + falling
    top = sum(info[i][2] for i in range(n))
    # best[d]: longest prefix built so far that ends at depth d
    best = [-1] * (top + 1)
    best[0] = 0
    taken = []
    for i in order:
        change, low, size = info[i]
        new = best[:]
        took = bytearray(top + 1)
        for d in range(top + 1):
            if best[d] < 0 or d + low < 0:
                continue
            e = d + change
            if best[d] + size > new[e]:
                new[e] = best[d] + size
                took[e] = 1
        best = new
        taken.append(took)
    used = []
    d = 0
    for step in range(len(order) - 1, -1, -1):
        if taken[step][d]:
            i = order[step]
            used.append(i + 1)
            d -= info[i][0]
    used.reverse()
    print(best[0], len(used))
    print(" ".join(map(str, used)))


main()
