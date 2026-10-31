import heapq
import sys

CHUNK_SIZE = 256


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    # base exceeds every kind; a key orders (-count, kind) without tuple objects.
    base = k + 1
    heap = [-int(c) * base + t for t, c in enumerate(data[1 : k + 1], 1)]
    # free the token list before the main loop
    del data
    heapq.heapify(heap)
    # fixed output chunks avoid holding every integer and its decimal rendering.
    order = []
    first = True
    prev = 0
    while heap:
        value = heapq.heappop(heap)
        count, t = divmod(value, base)
        if t == prev and heap:
            # the most plentiful kind was just used: take the next one
            other = heapq.heappop(heap)
            heapq.heappush(heap, value)
            value = other
            count, t = divmod(value, base)
        order.append(str(t))
        if len(order) == CHUNK_SIZE:
            sys.stdout.write(("" if first else " ") + " ".join(order))
            first = False
            order.clear()
        prev = t
        if count + 1 < 0:
            heapq.heappush(heap, value + base)
    sys.stdout.write(("" if first or not order else " ") + " ".join(order) + "\n")


main()
