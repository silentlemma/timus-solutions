import sys


def set_bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def main():
    tokens = sys.stdin.buffer.read().split()
    n, m = int(tokens[0]), int(tokens[1])
    owned_text = tokens[2 + 2 * m]
    if m == 0:
        print(owned_text.decode())
        return
    # Figure j is bit n - 1 - j of a set, and wish i is bit m - 1 - i of a
    # wish mask. needs[j] holds the wishes that require figure j: it is
    # column j of the matrix whose rows are the prerequisite strings.
    matrix = b"".join(tokens[2:2 + 2 * m:2])
    needs = [int(matrix[j::n], 2) for j in range(n)]
    adds = [int(t, 2) for t in tokens[2 + 1:2 + 1 + 2 * m:2]]
    owned = int(owned_text, 2)

    # A segment tree over figures keeps the OR of needs[j] over the figures
    # still missing, which is the set of wishes not yet enabled.
    size = 1
    while size < n:
        size *= 2
    tree = [0] * (2 * size)
    for j in range(n):
        if not owned >> (n - 1 - j) & 1:
            tree[size + j] = needs[j]
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] | tree[2 * i + 1]

    every = (1 << m) - 1
    fired = 0
    while True:
        ready = every & ~tree[1] & ~fired
        if not ready:
            break
        fired |= ready
        gain = 0
        for bit in set_bits(ready):
            gain |= adds[m - 1 - bit]
        fresh = gain & ~owned
        owned |= fresh
        for bit in set_bits(fresh):
            i = size + n - 1 - bit
            tree[i] = 0
            i //= 2
            while i:
                tree[i] = tree[2 * i] | tree[2 * i + 1]
                i //= 2

    print(format(owned, "0%db" % n))


main()
