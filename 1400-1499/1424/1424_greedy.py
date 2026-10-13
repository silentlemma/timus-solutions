import heapq
import sys


def main():
    vals = map(int, sys.stdin.buffer.read().split())
    n, m, k, price = next(vals), next(vals), next(vals), next(vals)
    starts = [[] for _ in range(n + 1)]
    ends = [0] * (n + 1)
    finish = [0] * (k + 1)
    for i in range(1, k + 1):
        s, f = next(vals), next(vals)
        starts[s].append(i)
        finish[i] = f
    taken = [False] * (k + 1)
    heap = []  # riders on board by the farthest stop first
    riding = 0
    for stop in range(1, n + 1):
        riding -= ends[stop]
        for i in starts[stop]:
            taken[i] = True
            heapq.heappush(heap, (-finish[i], i))
            ends[finish[i]] += 1
            riding += 1
        # too many: drop whoever would ride the longest
        while riding > m:
            _, i = heapq.heappop(heap)
            taken[i] = False
            ends[finish[i]] -= 1
            riding -= 1
    chosen = [i for i in range(1, k + 1) if taken[i]]
    print(len(chosen) * price)
    print(" ".join(map(str, chosen)))


main()
