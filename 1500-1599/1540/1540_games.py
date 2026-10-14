import heapq
import sys


def analyse(rings):
    """Grundy value of a chain and, for every gold content x, the xor of the
    pieces left after removing all rings with at most x."""
    # every piece that can ever appear is a maximal run of rings above some
    # content; such runs nest, and the children of a run are the runs above
    # its smallest content
    low, children, grundy = [], [], []

    def build(left, right):
        node = len(low)
        low.append(min(rings[left : right + 1]))
        children.append([])
        grundy.append(0)
        i = left
        while i <= right:
            if rings[i] > low[node]:
                j = i
                while j + 1 <= right and rings[j + 1] > low[node]:
                    j += 1
                children[node].append(build(i, j))
                i = j
            i += 1
        return node

    def after_moves(node):
        """{x: xor of the pieces left by removing rings up to x} in node."""
        result = {}
        heap = [(low[c], c) for c in children[node]]
        heapq.heapify(heap)
        xor = 0
        for c in children[node]:
            xor ^= grundy[c]
        result[low[node]] = xor
        while heap:
            x = heap[0][0]
            while heap and heap[0][0] == x:
                _, c = heapq.heappop(heap)
                xor ^= grundy[c]
                for d in children[c]:
                    xor ^= grundy[d]
                    heapq.heappush(heap, (low[d], d))
            result[x] = xor
        return result

    root = build(0, len(rings) - 1)
    # children are built after their parents, so go backwards
    for node in range(len(low) - 1, -1, -1):
        options = set(after_moves(node).values())
        g = 0
        while g in options:
            g += 1
        grundy[node] = g
    return grundy[root], after_moves(root)


def main():
    data = list(map(int, sys.stdin.read().split()))
    k = data[0]
    chains = []
    pos = 1
    for _ in range(k):
        length = data[pos]
        chains.append(data[pos + 1 : pos + 1 + length])
        pos += 1 + length
    results = [analyse(c) for c in chains]
    total = 0
    for g, _ in results:
        total ^= g
    if total == 0:
        print("S")
        return
    # a winning move leaves the chain with the xor of all other chains
    for i, (chain, (g, after)) in enumerate(zip(chains, results)):
        for j, x in enumerate(chain):
            if after[x] == total ^ g:
                print("G")
                print(i + 1, j + 1)
                return


main()
