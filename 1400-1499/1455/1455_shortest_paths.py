import heapq
import sys


def main():
    data = sys.stdin.read().split()
    words = data[1 : 1 + int(data[0])]
    # a state is the tail by which one parse runs ahead of the other; the
    # cost is the length of the text so far, and Dijkstra finds the shortest text
    dist, back = {}, {}
    heap = []
    for u in words:
        for v in words:
            if u != v and v.startswith(u):
                tail = v[len(u) :]
                if len(v) < dist.get(tail, len(v) + 1):
                    dist[tail], back[tail] = len(v), (None, v)
                    heapq.heappush(heap, (len(v), tail))
    while heap:
        cost, tail = heapq.heappop(heap)
        if cost > dist[tail]:
            continue
        for w in words:
            if w == tail:
                # both parses end together: rebuild the text from its pieces
                pieces = []
                while tail is not None:
                    tail, piece = back[tail]
                    pieces.append(piece)
                print("YES")
                print("".join(reversed(pieces)))
                return
            if w.startswith(tail):
                nxt, step, piece = w[len(tail) :], len(w) - len(tail), w[len(tail) :]
            elif tail.startswith(w):
                nxt, step, piece = tail[len(w) :], 0, ""
            else:
                continue
            if cost + step < dist.get(nxt, cost + step + 1):
                dist[nxt], back[nxt] = cost + step, (tail, piece)
                heapq.heappush(heap, (cost + step, nxt))
    print("NO")


main()
