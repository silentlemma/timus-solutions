import sys
from math import gcd

SHORT = 3  # any three points on both sides match


def directions(trees):
    """The distinct directions as reduced p / q with q > 0, by increasing p / q."""
    seen = set()
    for x, y in trees:
        if y < 0:
            x, y = -x, -y
        g = gcd(x, y)
        seen.add((x // g, y // g))
    return sorted(seen, key=lambda d: d[0] / d[1])


def ratios(dirs, ids):
    """Cross-ratio of every four consecutive directions, as small integer ids."""
    out = []
    for i in range(len(dirs) - SHORT):
        (p1, q1), (p2, q2), (p3, q3), (p4, q4) = dirs[i : i + SHORT + 1]
        # (c - a)(d - b) / ((c - b)(d - a)); the denominators q cancel
        num = (p3 * q1 - p1 * q3) * (p4 * q2 - p2 * q4)
        den = (p3 * q2 - p2 * q3) * (p4 * q1 - p1 * q4)
        g = gcd(num, den)
        out.append(ids.setdefault((num // g, den // g), len(ids)))
    return out


def longest_common(a, b, symbols):
    """Longest common substring of two sequences, by a suffix automaton of a."""
    link, length = [-1], [0]
    # trans[state * symbols + symbol]: the next state; each state lists its symbols
    trans = {}
    head, edge_symbol, edge_next = [-1], [], []

    def add(state, symbol, target):
        trans[state * symbols + symbol] = target
        edge_symbol.append(symbol)
        edge_next.append(head[state])
        head[state] = len(edge_symbol) - 1

    last = 0
    for ch in a:
        cur = len(length)
        length.append(length[last] + 1)
        link.append(0)
        head.append(-1)
        p = last
        while p != -1 and p * symbols + ch not in trans:
            add(p, ch, cur)
            p = link[p]
        if p != -1:
            q = trans[p * symbols + ch]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                clone = len(length)
                length.append(length[p] + 1)
                link.append(link[q])
                head.append(-1)
                e = head[q]
                while e != -1:
                    add(clone, edge_symbol[e], trans[q * symbols + edge_symbol[e]])
                    e = edge_next[e]
                while p != -1 and trans.get(p * symbols + ch) == q:
                    trans[p * symbols + ch] = clone
                    p = link[p]
                link[q] = link[cur] = clone
        last = cur
    best = state = run = 0
    for ch in b:
        while state and state * symbols + ch not in trans:
            state = link[state]
            run = length[state]
        if state * symbols + ch in trans:
            state = trans[state * symbols + ch]
            run += 1
        best = max(best, run)
    return best


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    upper, lower = [], []
    for i in range(0, len(data) - 1, 2):
        x, y = data[i], data[i + 1]
        if x == 0 and y == 0:
            break
        (upper if y > 0 else lower).append((x, y))
    up, low = directions(upper), directions(lower)
    answer = min(len(up), len(low), SHORT)
    if len(up) > SHORT and len(low) > SHORT:
        ids = {}
        ra, rb = ratios(up, ids), ratios(low, ids)
        common = longest_common(ra, rb, len(ids))
        if common:
            answer = common + SHORT
    print(answer)


main()
