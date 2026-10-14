import sys

MOD = 10007
MOST = 512  # the product of the sizes is at most this


def sizes(text):
    """The length of the arrays at each depth, ending with 0 for the empty ones."""
    open_counts, dims = [], []
    for ch in text:
        if ch == "[":
            if open_counts:
                open_counts[-1] += 1
            open_counts.append(0)
        elif ch == "]":
            depth = len(open_counts) - 1
            while len(dims) <= depth:
                dims.append(0)
            dims[depth] = open_counts.pop()
    return dims


def main():
    dims = sizes(sys.stdin.read().strip())
    if len(dims) == 1:
        print(1)
        return
    # Stirling numbers of the second kind: ways to split m references into k objects
    stirling = [[0] * (MOST + 1) for _ in range(MOST + 1)]
    stirling[0][0] = 1
    for m in range(1, MOST + 1):
        prev, row = stirling[m - 1], stirling[m]
        for k in range(1, m + 1):
            row[k] = (prev[k - 1] + k * prev[k]) % MOD
    # m references to empty arrays: any partition of them (Bell numbers)
    ways = [sum(stirling[m]) % MOD for m in range(MOST + 1)]
    # the references at depth i number at most dims[0] * ... * dims[i - 1]
    slots = [1]
    for d in dims[:-1]:
        slots.append(slots[-1] * d)
    for i in range(len(dims) - 2, 0, -1):
        width = dims[i]
        # m references to arrays of this depth: k distinct arrays, whose
        # k * width elements are configured one level down
        upper = min(MOST // width, slots[i])
        nxt = [0] * (MOST + 1)
        for m in range(1, upper + 1):
            row = stirling[m]
            nxt[m] = sum(row[k] * ways[k * width] for k in range(1, m + 1)) % MOD
        ways = nxt
    print(ways[dims[0]])


main()
