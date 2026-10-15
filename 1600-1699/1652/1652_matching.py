import sys
from bisect import bisect_right

FIELDS = 3  # creditor, debtor, sum
DEPTH = 10000  # augmenting paths nest a call per bank


def most_responsible(banks, debts, money):
    """a maximum matching of banks to debts of their own country: a bank
    keeps a debt it already holds or buys one it can afford"""
    debts.sort(key=lambda d: d[2])
    costs = [d[2] for d in debts]
    nd = len(debts)
    reach = {b: bisect_right(costs, money[b]) for b in banks}  # affordable prefix
    own = {b: [] for b in banks}
    for j, (creditor, _, _) in enumerate(debts):
        if creditor in own:
            own[creditor].append(j)
    holder = [-1] * nd
    seen = [False] * nd
    skip = list(range(nd + 1))  # skip[j]: the first unseen debt from j on

    def unseen(j):
        root = j
        while skip[root] != root:
            root = skip[root]
        while skip[j] != root:
            skip[j], j = root, skip[j]
        return root

    def visit(j):
        seen[j] = True
        skip[j] = j + 1

    def augment(b):
        for j in own[b]:
            if not seen[j]:
                visit(j)
                if holder[j] < 0 or augment(holder[j]):
                    holder[j] = b
                    return True
        j = unseen(0)
        while j < reach[b]:
            if debts[j][1] != b:  # a bank cannot hold its own debt
                visit(j)
                if holder[j] < 0 or augment(holder[j]):
                    holder[j] = b
                    return True
            j = unseen(j + 1)
        return False

    count = 0
    # banks that hold a debt already go first, then the poorer ones
    for b in sorted(banks, key=lambda b: (not own[b], reach[b])):
        # marks are cleared only after a success: when a search fails the
        # matching stays as it was, so the debts it saw still lead nowhere
        if augment(b):
            count += 1
            seen[:] = [False] * nd
            skip[:] = range(nd + 1)
    return count


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    country, money = data[1 : 1 + 2 * n : 2], data[2 : 2 + 2 * n : 2]
    m = data[1 + 2 * n]
    contracts = data[2 + 2 * n : 2 + 2 * n + FIELDS * m]
    banks, debts = {}, {}
    for b in range(n):
        banks.setdefault(country[b], []).append(b)
    for i in range(m):
        creditor, debtor, amount = contracts[FIELDS * i : FIELDS * (i + 1)]
        debts.setdefault(country[debtor - 1], []).append((creditor - 1, debtor - 1, amount))
    sys.setrecursionlimit(DEPTH)
    total = 0
    for c, group in banks.items():
        total += most_responsible(group, debts.get(c, []), money)
    print(total)


main()
