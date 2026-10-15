import sys

MOST = 10 ** 9  # nobody but Vasily earns more than this; nobody earns less than 0
FIELDS = 3  # i j d


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    # a weighted union-find: salary[x] = salary[root] + offset[x], and every
    # root keeps the range its own salary may take so that all salaries of
    # its set stay in [0, MOST]; Vasily (0) is pinned to 0
    parent = list(range(n))
    offset = [0] * n
    size = [1] * n
    low = [0] * n
    high = [MOST] * n
    high[0] = 0

    def find(x):
        path = []
        while parent[x] != x:
            path.append(x)
            x = parent[x]
        # compress: walk back from the node nearest to the root
        total = 0
        for v in reversed(path):
            total += offset[v]
            offset[v] = total
            parent[v] = x
        return x

    for k in range(m):
        i, j, d = (int(w) for w in data[2 + FIELDS * k:2 + FIELDS * (k + 1)])
        ri, rj = find(i), find(j)
        oi = offset[i] if i != ri else 0
        oj = offset[j] if j != rj else 0
        # salary[i] - salary[j] = d means salary[rj] = salary[ri] + shift
        shift = oi - oj - d
        if ri == rj:
            ok = shift == 0
        else:
            if size[ri] < size[rj]:
                ri, rj, shift = rj, ri, -shift
            # salary[rj] lies in [low[rj], high[rj]], so salary[ri] in that minus shift
            low[ri] = max(low[ri], low[rj] - shift)
            high[ri] = min(high[ri], high[rj] - shift)
            ok = low[ri] <= high[ri]
            parent[rj], offset[rj] = ri, shift
            size[ri] += size[rj]
        if not ok:
            print("Impossible after %d statements" % (k + 1))
            return
    out = ["Possible"]
    for x in range(n):
        r = find(x)
        out.append(str(low[r] + (offset[x] if x != r else 0)))
    print("\n".join(out))


main()
