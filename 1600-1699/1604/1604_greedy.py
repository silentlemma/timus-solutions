import heapq
import sys


def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    heap = [(-int(c), t) for t, c in enumerate(data[1 : k + 1], 1)]
    heapq.heapify(heap)
    order = []
    prev = 0
    while heap:
        count, t = heapq.heappop(heap)
        if t == prev and heap:
            # the most plentiful kind was just used: take the next one
            other, u = heapq.heappop(heap)
            heapq.heappush(heap, (count, t))
            count, t = other, u
        order.append(t)
        prev = t
        if count + 1 < 0:
            heapq.heappush(heap, (count + 1, t))
    print(" ".join(map(str, order)))


main()
