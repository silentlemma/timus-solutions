import sys

SEATS = 4  # compartment seats in a block
SIDES = 2  # side seats in a block


def main():
    words = iter(sys.stdin.read().split())
    n, wish, m = int(next(words)), next(words), int(next(words))
    people = (SEATS + SIDES) * n
    parent = list(range(people))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for _ in range(m):
        a, b = int(next(words)) - 1, int(next(words)) - 1
        parent[find(a)] = find(b)
    groups = {}
    for p in range(people):
        groups.setdefault(find(p), []).append(p + 1)
    # a group of friends wants a compartment seats and b side seats; a block
    # holds one group with b = 2, or two groups with b = 1, and groups with
    # b = 0 fill the compartment seats left: kind[b][a]
    kind = [[[] for _ in range(SEATS + 1)] for _ in range(SIDES + 1)]
    for g in groups.values():
        a = sum(wish[p - 1] == "1" for p in g)
        kind[len(g) - a][a].append(g)
    fillers, halves, wholes = kind
    s0, s1, s2, s3, s4 = (len(x) for x in halves)
    t0, t1, t2, _, _ = (len(x) for x in wholes)
    _, _, f2, f3, f4 = (len(x) for x in fillers)

    def fits(c4, c3, c2):
        # can the fillers fill blocks with c4, c3, c2 free compartment seats
        # (and some with 1)? fours need a 4, threes take a 3 first and then
        # a 4, twos take what is left of the 2s, 3s and 4s
        if f4 > c4 or f3 > c3 + c4 - f4:
            return False
        late = max(0, f3 - c3)  # threes in blocks with 4 free seats
        return f2 <= c2 + (c3 - f3 + late) + 2 * (c4 - f4 - late)

    # two halves with a1 and a2 leave 4 - a1 - a2 free seats; merging the
    # free seats of two blocks never hurts, so threes pair with ones when
    # they can, and two (0, 2) pairs would rather be (2, 2) and (0, 0)
    x31 = min(s3, s1)
    x30 = s3 - x31
    ones = s1 - x31
    zeros = s0 - s4 - x30
    plan = None
    for x20 in (0, 1):
        for x21 in range(min(s2 - x20, ones) + 1):
            # with x11 pairs (1, 1) the zeros left pair up as base + 2 x11
            base = zeros - x20 - ones + x21
            if plan or (s2 - x21 - x20) % 2 or base % 2:
                continue
            # x11 must leave both kinds of pairs possible and give the fours
            # and the threes their blocks; the room for twos rises until the
            # free threes run short of threes and falls after that
            low = max(0, -base // 2, f4 - t0 - base // 2)
            high = min((ones - x21) // 2, t0 + t1 + ones - x21 + base // 2 - f3 - f4)
            peak = min(max((t1 + ones - x21 - f3) // 2, low), high)
            for x11 in (peak - 1, peak, peak + 1):
                x10, x00 = ones - x21 - 2 * x11, base // 2 + x11
                if low <= x11 <= high and fits(t0 + x00, t1 + x10, t2 + x20 + x11):
                    plan = {(SEATS, 0): s4, (SEATS - 1, 1): x31, (SEATS - 1, 0): x30,
                            (2, 2): (s2 - x21 - x20) // 2, (2, 1): x21, (2, 0): x20,
                            (1, 1): x11, (1, 0): x10, (0, 0): x00}
                    break
    blocks = []  # [members, free compartment seats]
    for a, single in enumerate(wholes):
        blocks += [[g[:], SEATS - a] for g in single]
    for (a, b), count in plan.items():
        for _ in range(count):
            blocks.append([halves[a].pop() + halves[b].pop(), SEATS - a - b])
    # the fillers, largest first, as the check above assumes
    free = [[] for _ in range(SEATS + 1)]
    for i, (_, seats) in enumerate(blocks):
        free[seats].append(i)
    for size in range(SEATS, 0, -1):
        for group in fillers[size]:
            seats = next(c for c in range(size, SEATS + 1) if free[c])
            i = free[seats].pop()
            blocks[i][0] += group
            free[seats - size].append(i)
    print("\n".join(" ".join(map(str, members)) for members, _ in blocks))


main()
