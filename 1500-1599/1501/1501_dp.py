import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    piles = data[1], data[2]

    # after taking i cards of the first pile and j of the second, the red and
    # the black piles differ by d1[i] + d2[j], where d = 2 * reds - taken
    def balance(pile):
        d = [0]
        for card in pile:
            d.append(d[-1] + (1 if card == "1" else -1))
        return d

    d1, d2 = balance(piles[0]), balance(piles[1])
    by_balance = {}
    for j, v in enumerate(d2):
        by_balance[v] = by_balance.get(v, 0) | 1 << j

    # rows[i]: bit j is set when the state (i, j) can be reached; within a
    # row a state is reached from the one above it or, through a run of
    # allowed states, from the left, which an addition spreads in one step
    rows = []
    above = 1  # (0, 0) is reached from nowhere
    for i in range(n + 1):
        allowed = 0
        for v in (-d1[i] - 1, -d1[i], -d1[i] + 1):
            allowed |= by_balance.get(v, 0)
        start = allowed & above
        reach = (((allowed + start) ^ allowed) & allowed) | start
        rows.append(reach)
        above = reach
    if not rows[n] >> n & 1:
        print("Impossible")
        return

    # walk back from (n, n): a step left took a card of the second pile
    moves = []
    i, j = n, n
    while i or j:
        if j and rows[i] >> (j - 1) & 1:
            moves.append("2")
            j -= 1
        else:
            moves.append("1")
            i -= 1
    print("".join(reversed(moves)))


main()
