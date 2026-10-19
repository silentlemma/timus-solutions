import sys

KEYS = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
PRESSES = {ord(ch): k + 1 for key in KEYS for k, ch in enumerate(key)}
SLOWEST = max(len(key) for key in KEYS)


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    words = data[1:n + 1]
    # state offset[x] + d: name x is current and its first d letters are
    # typed; trie node of the typed letters is node_of[state]
    offset = [0] * (n + 1)
    for x, w in enumerate(words):
        offset[x + 1] = offset[x] + len(w) + 1
    states = offset[n]
    node_of = [0] * states
    owner = [0] * states
    low, high = [0], [n - 1]  # the names below a node form a range
    children = [[]]  # (state of the first name below the child, letter cost)
    path = [0]
    previous = b""
    for x, w in enumerate(words):
        same = 0
        while same < len(w) and same < len(previous) and w[same] == previous[same]:
            same += 1
        del path[same + 1:]
        for d in range(same + 1, len(w) + 1):
            v = len(low)
            low.append(x)
            high.append(x)
            children.append([])
            children[path[-1]].append((offset[x] + d, PRESSES[w[d - 1]]))
            path.append(v)
        base = offset[x]
        for d in range(len(w) + 1):
            node_of[base + d] = path[d]
            owner[base + d] = x
            high[path[d]] = x
        previous = w
    hubs = len(low)
    infinity = float("inf")
    dist = [infinity] * (states + hubs)
    # every move costs at most SLOWEST, so SLOWEST + 1 buckets in a circle
    buckets = [[] for _ in range(SLOWEST + 1)]
    dist[0] = 0
    buckets[0].append(0)
    pending, now = 1, 0
    while pending:
        bucket = buckets[now % (SLOWEST + 1)]
        while bucket:
            s = bucket.pop()
            pending -= 1
            if dist[s] != now:
                continue
            if s >= states:
                moves = children[s - states]
            else:
                x = owner[s]
                d = s - offset[x]
                v = node_of[s]
                nxt = x + 1 if x < high[v] else low[v]
                prv = x - 1 if x > low[v] else high[v]
                moves = [(offset[nxt] + d, 1), (offset[prv] + d, 1), (states + v, 0)]
                if d:
                    moves.append((s - 1, 1))
            for t, cost in moves:
                if now + cost < dist[t]:
                    dist[t] = now + cost
                    buckets[(now + cost) % (SLOWEST + 1)].append(t)
                    pending += 1
        now += 1
    best = [min(dist[offset[x]:offset[x + 1]]) for x in range(n)]
    print(*best)


main()
