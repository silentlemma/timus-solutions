import heapq
import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    orders = sorted(range(n), key=lambda i: data[1 + 2 * i])
    # by deadline: keep the best orders that fit, dropping the cheapest when
    # there are more orders than days so far
    kept = []
    for i in orders:
        heapq.heappush(kept, (data[2 + 2 * i], i))
        if len(kept) > data[1 + 2 * i]:
            heapq.heappop(kept)
    chosen = sorted((i for _, i in kept), key=lambda i: data[1 + 2 * i])
    print(len(chosen))
    print(" ".join(str(i + 1) for i in chosen))


main()
