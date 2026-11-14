from itertools import combinations
import sys

GROUP_BITS = 5
GROUPS = 4
GROUP_SIZE = 1 << GROUP_BITS
GROUP_MASK = GROUP_SIZE - 1
HOME = 1
WORK = 2


def solve(categories, graph):
    def connects(permits):
        a = permits & GROUP_MASK
        b = (permits >> GROUP_BITS) & GROUP_MASK
        c = (permits >> (2 * GROUP_BITS)) & GROUP_MASK
        d = permits >> ((GROUPS - 1) * GROUP_BITS)
        seen = pending = HOME
        while pending:
            bit = pending & -pending
            pending ^= bit
            p, q, r, s = graph[bit.bit_length() - 1]
            fresh = (p[a] | q[b] | r[c] | s[d]) & ~seen
            if fresh & WORK:
                return True
            seen |= fresh
            pending |= fresh
        return False

    all_permits = (1 << categories) - 1
    required = 0
    optional = []
    for category in range(categories):
        bit = 1 << category
        if connects(all_permits ^ bit):
            optional.append(bit)
        else:
            required |= bit
    # Distinct category bits are disjoint, so summing the bits forms the mask.
    for size in range(len(optional) + 1):
        for subset in combinations(optional, size):
            permits = required | sum(subset)
            if connects(permits):
                return [index for index in range(categories) if permits >> index & 1]
    return []


def main():
    read = sys.stdin.buffer.readline
    categories, crossings, count = map(int, read().split())
    graph = [[[0] * GROUP_SIZE for _ in range(GROUPS)] for _ in range(crossings)]
    for _ in range(count):
        a, b, category = map(int, read().split())
        group, offset = divmod(category, GROUP_BITS)
        bit = 1 << offset
        graph[a][group][bit] |= 1 << b
        graph[b][group][bit] |= 1 << a
    for row in graph:
        for table in row:
            for mask in range(1, GROUP_SIZE):
                rest = mask & (mask - 1)
                table[mask] |= table[rest] | table[mask ^ rest]
    permits = solve(categories, graph)
    print(len(permits))
    print(*permits)


if __name__ == "__main__":
    main()
