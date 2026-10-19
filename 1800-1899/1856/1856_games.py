import sys
from array import array


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [int(v) - 1 for v in data[1:2 * n + 1:2]]
    b = [int(v) - 1 for v in data[2:2 * n + 2:2]]
    spells = (a, b)
    # the army gathers exactly when every pair of garrisons can be forced
    # together, one pair after another; a pair (u, v), u < v, is the number
    # u * n + v, and a day is her spell m, then his spell k
    size = n * n
    open_moves = bytearray(2 * size)  # replies of his that keep the pair apart
    targets = array("i")  # (pair after both spells, pair * 2 + her spell)
    for u in range(n):
        for v in range(u + 1, n):
            p = u * n + v
            for mine, m in enumerate(spells):
                x, y = m[u], m[v]
                if x == y:
                    continue
                for k in spells:
                    s, t = k[x], k[y]
                    if s != t:
                        targets.append(s * n + t if s < t else t * n + s)
                        targets.append(2 * p + mine)
                        open_moves[2 * p + mine] += 1
    # the replies that lead into every pair, grouped by that pair
    start = array("i", [0]) * (size + 1)
    for i in range(0, len(targets), 2):
        start[targets[i] + 1] += 1
    for q in range(size):
        start[q + 1] += start[q]
    place = array("i", start)
    sources = array("i", [0]) * (len(targets) // 2)
    for i in range(0, len(targets), 2):
        q = targets[i]
        sources[place[q]] = targets[i + 1]
        place[q] += 1
    # a pair is won when some spell of hers leaves him no reply that keeps
    # the pair apart outside the won pairs
    won = bytearray(size)
    queue = []
    for u in range(n):
        for v in range(u + 1, n):
            p = u * n + v
            if not open_moves[2 * p] or not open_moves[2 * p + 1]:
                won[p] = 1
                queue.append(p)
    for q in queue:
        for e in range(start[q], start[q + 1]):
            move = sources[e]
            p = move >> 1
            if won[p]:
                continue
            open_moves[move] -= 1
            if not open_moves[move]:
                won[p] = 1
                queue.append(p)
    print("War" if len(queue) == n * (n - 1) // 2 else "Peace")


main()
