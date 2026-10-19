import sys
from bisect import bisect_right
from itertools import accumulate

PERCENT = 100
MAX_PRICE = 50000


def main():
    data = map(int, sys.stdin.buffer.read().split())
    n = next(data)
    m = next(data)
    prices = [[] for _ in range(PERCENT + 1)]
    baseline = 0
    for _ in range(n):
        price = next(data)
        discount = next(data)
        prices[discount].append(price)
        baseline += price * (PERCENT - discount)

    required = [n + 1] * (PERCENT + 1)
    for _ in range(m):
        count = next(data)
        discount = next(data)
        if count < required[discount]:
            required[discount] = count
    del data

    prefix = []
    counts = []
    totals = []
    weighted = []
    count = total = weight = 0
    for discount, group in enumerate(prices):
        group.sort()
        sums = list(accumulate(group, initial=0))
        prefix.append(sums)
        count += len(group)
        total += sums[-1]
        weight += discount * sums[-1]
        counts.append(count)
        totals.append(total)
        weighted.append(weight)

    answer = baseline
    smallest_count = n + 1
    for discount in range(PERCENT, 0, -1):
        if required[discount] >= smallest_count:
            continue
        smallest_count = required[discount]
        cost = baseline + weighted[discount] - discount * totals[discount]
        if cost >= answer:
            continue
        need = smallest_count - counts[discount]
        if need > 0:
            groups = [
                (other - discount, prices[other], prefix[other])
                for other in range(discount + 1, PERCENT + 1)
                if prices[other]
            ]
            low = 0
            high = MAX_PRICE * (PERCENT - discount)
            while low < high:
                middle = (low + high) // 2
                taken = 0
                for factor, group, _ in groups:
                    taken += bisect_right(group, middle // factor)
                if taken >= need:
                    high = middle
                else:
                    low = middle + 1

            # All excess tickets at the boundary have the same extra cost.
            taken = 0
            for factor, group, sums in groups:
                size = bisect_right(group, low // factor)
                taken += size
                cost += factor * sums[size]
            cost -= (taken - need) * low
        answer = min(answer, cost)

    print(f"{answer // PERCENT}.{answer % PERCENT:02d}")


if __name__ == "__main__":
    main()
