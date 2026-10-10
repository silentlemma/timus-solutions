import sys

SIDE = 4
ROOMS = SIDE * SIDE
# moves inside a level: name, row step, column step
MOVES = (("N", -1, 0), ("E", 0, 1), ("S", 1, 0), ("W", 0, -1))


def neighbours(u):
    r, c = divmod(u, SIDE)
    for name, dr, dc in MOVES:
        if 0 <= r + dr < SIDE and 0 <= c + dc < SIDE:
            yield name, (r + dr) * SIDE + c + dc


ADJ = [list(neighbours(u)) for u in range(ROOMS)]


def level_table(food):
    # best[s][e][k]: most food on a path of k rooms from s to e in one level
    best = [[[-1] * (ROOMS + 1) for _ in range(ROOMS)] for _ in range(ROOMS)]

    def walk(row, u, mask, k, total):
        if total > row[u][k]:
            row[u][k] = total
        for _, v in ADJ[u]:
            if not mask >> v & 1:
                walk(row, v, mask | 1 << v, k + 1, total + food[v])

    for s in range(ROOMS):
        walk(best[s], s, 1 << s, 1, food[s])
    return best


def find_moves(food, s, e, k, total):
    # some path of k rooms from s to e with exactly this much food
    path = []

    def walk(u, mask, left, rest):
        if left == 1:
            return u == e and rest == food[u]
        for name, v in ADJ[u]:
            if not mask >> v & 1:
                path.append(name)
                if walk(v, mask | 1 << v, left - 1, rest - food[u]):
                    return True
                path.pop()
        return False

    walk(s, 1 << s, k, total)
    return "".join(path)


def main():
    data = iter(map(int, sys.stdin.read().split()))
    n = next(data)
    foods, doors = [], []
    for _ in range(n):
        foods.append([next(data) for _ in range(ROOMS)])
        doors.append([next(data) for _ in range(ROOMS)])
    start = (next(data) - 1) * SIDE + next(data) - 1
    tables = [level_table(f) for f in foods]

    def best_path(num, den):
        # the path maximising den * food - num * rooms, as its choices per
        # level (start, end, rooms) with its food and room count
        after = [0] * ROOMS
        choice = [None] * n
        for lv in range(n - 1, -1, -1):
            last = lv == n - 1
            here, pick = [None] * ROOMS, [None] * ROOMS
            for s in range(ROOMS):
                for e in range(ROOMS):
                    if not last and not doors[lv][e]:
                        continue
                    if after[e] is None:
                        continue
                    for k in range(1, ROOMS + 1):
                        w = tables[lv][s][e][k]
                        if w >= 0:
                            v = den * w - num * k + after[e]
                            if here[s] is None or v > here[s]:
                                here[s], pick[s] = v, (e, k)
            after, choice[lv] = here, pick
        plan, total, rooms, s = [], 0, 0, start
        for lv in range(n):
            e, k = choice[lv][s]
            plan.append((s, e, k))
            total += tables[lv][s][e][k]
            rooms += k
            s = e
        return plan, total, rooms

    # Dinkelbach: move to the better ratio until no path beats the current
    num, den = 0, 1
    while True:
        plan, total, rooms = best_path(num, den)
        if total * den <= num * rooms:
            break
        num, den = total, rooms
        best = plan
    moves = "D".join(
        find_moves(foods[lv], s, e, k, tables[lv][s][e][k]) for lv, (s, e, k) in enumerate(best)
    )
    print("%.4f" % (num / den))
    print(len(moves))
    if moves:
        print(moves)


main()
