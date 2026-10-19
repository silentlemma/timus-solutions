import sys


def maximum_matching(rows, m):
    left = [-1] * len(rows)
    right = [-1] * m
    free = (1 << m) - 1
    for start, row in enumerate(rows):
        if not free:
            break
        available = row & free
        if available:
            bit = available & -available
            v = bit.bit_length() - 1
            left[start] = v
            right[v] = start
            free -= bit
            continue
        queue = [start]
        at = seen = 0
        parent = [-1] * m
        finish = -1
        while at < len(queue) and finish < 0:
            u = queue[at]
            at += 1
            unused = rows[u] & ~seen
            while unused:
                bit = unused & -unused
                unused -= bit
                seen |= bit
                v = bit.bit_length() - 1
                parent[v] = u
                if right[v] < 0:
                    finish = v
                    break
                queue.append(right[v])
        if finish >= 0:
            free &= ~(1 << finish)
            while finish >= 0:
                u = parent[finish]
                old = left[u]
                left[u] = finish
                right[finish] = u
                finish = old
    return left, right


def reach(rows, opposite_matching, roots):
    own = other = 0
    queue = list(roots)
    for u in queue:
        own |= 1 << u
    for u in queue:
        unused = rows[u] & ~other
        while unused:
            bit = unused & -unused
            unused -= bit
            other |= bit
            v = bit.bit_length() - 1
            partner = opposite_matching[v]
            if partner >= 0 and not (own >> partner) & 1:
                own |= 1 << partner
                queue.append(partner)
    return own, other


def solve(rows, reverse):
    n = len(rows)
    m = len(reverse)
    left, right = maximum_matching(rows, m)
    never_left, always_right = reach(rows, right, (u for u in range(n) if left[u] < 0))
    never_right, always_left = reach(reverse, left, (v for v in range(m) if right[v] < 0))
    assert not never_left & always_left and not never_right & always_right
    a = "".join(
        "N" if (never_left >> u) & 1 else "A" if (always_left >> u) & 1 else "E" for u in range(n)
    )
    b = "".join(
        "N" if (never_right >> v) & 1 else "A" if (always_right >> v) & 1 else "E" for v in range(m)
    )
    return a, b


def main():
    read = sys.stdin.buffer.readline
    n, m, k = map(int, read().split())
    rows = [0] * n
    reverse = [0] * m
    left_bits = [1 << u for u in range(n)]
    right_bits = [1 << v for v in range(m)]
    for _ in range(k):
        pair = read().split()
        u = int(pair[0]) - 1
        v = int(pair[1]) - 1
        rows[u] |= right_bits[v]
        reverse[v] |= left_bits[u]
    print(*solve(rows, reverse), sep="\n")


if __name__ == "__main__":
    main()
