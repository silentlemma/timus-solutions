import sys


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    # children 0..k-1 are boys and k..2k-1 girls; likes[v] is the child v
    # likes, or -1; nobody is liked by two, so the likes form paths and cycles
    likes = [-1] * (2 * k)
    liked = [False] * (2 * k)
    for i in range(k):
        g, b = int(data[1 + i]), int(data[1 + k + i])
        if g:
            likes[i] = k + g - 1
            liked[k + g - 1] = True
        if b:
            likes[k + i] = b - 1
            liked[b - 1] = True
    partner = [-1] * (2 * k)
    seen = [False] * (2 * k)

    def pair_along(start):
        """Pair the children along the likes from start, two by two; on an
        odd path the last one, who likes nobody, stays free."""
        chain, v = [], start
        while v >= 0 and not seen[v]:
            seen[v] = True
            chain.append(v)
            v = likes[v]
        for a, b in zip(chain[::2], chain[1::2]):
            partner[a], partner[b] = b, a

    for v in range(2 * k):
        if not liked[v]:
            pair_along(v)
    for v in range(2 * k):
        if not seen[v]:
            pair_along(v)  # what is left are cycles, always of even length
    # the free children like nobody and can be paired in any way
    free_girls = [v for v in range(k, 2 * k) if partner[v] < 0]
    free_boys = [v for v in range(k) if partner[v] < 0]
    for b, g in zip(free_boys, free_girls):
        partner[b] = g
    print(" ".join(str(partner[i] - k + 1) for i in range(k)))


main()
