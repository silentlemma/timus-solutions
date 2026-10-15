import sys
from collections import deque

INF = float("inf")


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    width = m + 2  # a border of walls around the map
    cells = "#" * width + "".join("#" + row + "#" for row in data[2 : 2 + n]) + "#" * width
    steps = [dr * width + dc for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc]
    gates = {}
    for i, ch in enumerate(cells):
        if ch.isalpha():
            gates.setdefault(ch, []).append(i)
    fortress = cells.index("*")
    # walls start below every distance, so one comparison rules them out
    blank = [-1 if ch == "#" else INF for ch in cells]

    def bfs(start, avoid):
        """days to every district; teleports are free, so 0-1 BFS"""
        dist = blank[:]
        if avoid is not None:
            dist[avoid] = -1
        dist[start] = 0
        used = set()  # teleport letters already spread
        queue = deque([start])
        while queue:
            at = queue.popleft()
            d = dist[at]
            ch = cells[at]
            if ch in gates and ch not in used:
                used.add(ch)
                for g in gates[ch]:
                    if dist[g] > d:
                        dist[g] = d
                        queue.appendleft(g)
            d += 1
            for step in steps:
                to = at + step
                if dist[to] > d:
                    dist[to] = d
                    queue.append(to)
        return [INF if v < 0 else v for v in dist]

    first = bfs(cells.index("$"), fortress)
    second = bfs(cells.index("!"), fortress)
    attack = bfs(fortress, None)  # moves are symmetric, so this is the way back
    # the earlier army waits at the meeting place, then both march together
    attack[fortress] = INF
    best = min(max(a, b) + c for a, b, c in zip(first, second, attack))
    print("Impossible" if best == INF else best)


main()
