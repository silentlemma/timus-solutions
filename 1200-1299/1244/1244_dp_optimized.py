import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    weight, n = data[:2]
    cards = data[2:]
    missing_weight = sum(cards) - weight
    select_missing = missing_weight < weight
    target = min(weight, missing_weight)
    mask = (1 << (target + 1)) - 1
    once, twice = [1], 0
    # Complementing subsets preserves their count. Only reachability prefixes
    # are needed for reconstruction; multiplicity needs just the current row.
    for card in cards:
        previous = once[-1]
        shifted = (previous << card) & mask
        twice = (twice | (twice << card) | (previous & shifted)) & mask
        once.append(previous | shifted)
        if (twice >> target) & 1:
            print(-1)
            return
    if not (once[-1] >> target) & 1:
        print(0)
        return
    chosen = [False] * n
    remaining = target
    for i in range(n - 1, -1, -1):
        if not (once[i] >> remaining) & 1:
            chosen[i] = True
            remaining -= cards[i]
    print(" ".join(str(i + 1) for i in range(n) if chosen[i] == select_missing))


main()
