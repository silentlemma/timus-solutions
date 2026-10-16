import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, r = data[0], data[1]
    coords = data[2:]
    xs, ys = coords[0:2 * n:2], coords[1:2 * n:2]
    # cover[i]: the cities a bottle dropped on city i destroys
    cover = [0] * n
    for i in range(n):
        for j in range(n):
            if (xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2 <= r * r:
                cover[i] |= 1 << j
    failed = {}

    def search(left, budget):
        # pick at most budget cities covering the set left, or None
        if not left:
            return []
        if budget == 0 or failed.get(left, -1) >= budget:
            return None
        gain = [(cover[v] & left).bit_count() for v in range(n)]
        if left.bit_count() > budget * max(gain):
            failed[left] = budget
            return None
        # the uncovered city with the fewest cities able to hit it
        u = min((v for v in range(n) if left >> v & 1), key=lambda v: cover[v].bit_count())
        options = [v for v in range(n) if cover[u] >> v & 1]
        options.sort(key=lambda v: -gain[v])
        tried = []
        for v in options:
            hit = cover[v] & left
            # skip a drop that hits only part of what a tried one hits
            if any(hit & ~t == 0 for t in tried):
                continue
            tried.append(hit)
            rest = search(left & ~hit, budget - 1)
            if rest is not None:
                return [v] + rest
        failed[left] = budget
        return None

    everything = (1 << n) - 1
    budget = 1
    while True:
        drops = search(everything, budget)
        if drops is not None:
            break
        budget += 1
    print(len(drops))
    print(*(v + 1 for v in drops))


main()
