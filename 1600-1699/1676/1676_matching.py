import sys

DEPTH = 10000  # recursion of the augmenting search


def bits(mask):
    """The positions of the set bits of mask."""
    while mask:
        low = mask & -mask
        mask ^= low
        yield low.bit_length() - 1


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    cells = "".join(data[2:])
    # adj[i]: bit j set when fighter j beats monster i
    adj = [int(cells[i * m:(i + 1) * m][::-1], 2) for i in range(n)]
    full = (1 << m) - 1
    owner = [-1] * m  # the monster each fighter is matched with
    match = [-1] * n  # the fighter each monster is matched with
    sys.setrecursionlimit(DEPTH)
    unseen = [0]

    def augment(u):
        """Kuhn's step, with the unvisited fighters kept as one bit set."""
        for j in bits(adj[u] & unseen[0]):
            if not unseen[0] >> j & 1:
                continue
            unseen[0] &= ~(1 << j)
            if owner[j] < 0 or augment(owner[j]):
                owner[j], match[u] = u, j
                return True
        return False

    for i in range(n):
        unseen[0] = full
        if not augment(i):
            # some monster cannot be beaten in any assignment
            row = "1" * m
            sys.stdout.write("\n".join([row] * n) + "\n")
            return

    # i may take fighter j if j is free or its own, or if j's monster k moves on:
    # with k -> k2 when k can take k2's fighter, k reaches i (closing a cycle)
    # or reaches a monster (k included) that some free fighter beats
    free = full
    for j in match:
        free &= ~(1 << j)
    reach = [0] * n
    for k in range(n):
        for j in bits(adj[k] & ~free):
            if owner[j] != k:
                reach[k] |= 1 << owner[j]
    for mid in range(n):
        for k in range(n):
            if reach[k] >> mid & 1:
                reach[k] |= reach[mid]
    loose = sum(1 << k for k in range(n) if adj[k] & free)
    helped = 0  # fighters whose monster can always move on
    back = [0] * n  # back[i]: fighters whose monster reaches monster i
    for k in range(n):
        if loose >> k & 1 or reach[k] & loose:
            helped |= 1 << match[k]
        for i in bits(reach[k]):
            back[i] |= 1 << match[k]
    lines = []
    for i in range(n):
        ok = adj[i] & (free | 1 << match[i] | helped | back[i])
        lines.append(format(full & ~ok, "0%db" % m)[::-1])
    sys.stdout.write("\n".join(lines) + "\n")


main()
