"""A cut cube and questions from a seed and a mode: mode 1 a small cube,
2 the largest cube with the most questions, 3 the largest cube with
questions about far corners, 4 a cube of side 3 with the largest
crystals; 5 the maximum body diagonal with just one question; 6 local
neighbours in a largest cube with unit crystals; 7 interior pairs at odd
side 29; 8 one interior anchor in a largest cube; 9 planar pairs at side
17 with dense runes ending at 10^9. Every contact gets its own rune,
every crystal a proper turn, and the crystals come in scrambled order.
Arguments: seed mode. All randomness is seeded.
"""

import random
import sys

MOST = 30
QUESTIONS = 10000
RUNES = 10 ** 9
# faces: bottom, top, right, left, front, back; the face at each place
# of a cycle goes to the place of the next one
QUARTER_TURNS = ((4, 2, 5, 3), (0, 4, 1, 5))


def rotations():
    turns = []
    for cycle in QUARTER_TURNS:
        p = list(range(6))
        for x, y in zip(cycle, cycle[1:] + cycle[:1]):
            p[y] = x
        turns.append(tuple(p))
    seen = {tuple(range(6))}
    todo = list(seen)
    while todo:
        p = todo.pop()
        for q in turns:
            r = tuple(p[q[k]] for k in range(6))
            if r not in seen:
                seen.add(r)
                todo.append(r)
    return sorted(seen)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    if mode >= 5:
        extended(seed, mode)
        return
    rng = random.Random(seed)
    n = {1: rng.randint(2, 4), 4: 3}.get(mode, MOST)
    side = 100 if mode == 4 else rng.randint(1, 100)
    cells = [(x, y, z) for x in range(n) for y in range(n) for z in range(n)]
    index = {c: i for i, c in enumerate(cells)}
    faces = [[0] * 6 for _ in cells]
    runes = rng.sample(range(1, RUNES + 1), 3 * n * n * (n - 1))
    steps = [((0, -1, 0), 0, 1), ((1, 0, 0), 2, 3), ((0, 0, 1), 4, 5)]
    for c in cells:
        for (dx, dy, dz), here, there in steps:
            other = (c[0] + dx, c[1] + dy, c[2] + dz)
            if other in index:
                rune = runes.pop()
                faces[index[c]][here] = rune
                faces[index[other]][there] = rune
    turns = rotations()
    order = list(range(len(cells)))
    rng.shuffle(order)
    lines = []
    for i in order:
        p = rng.choice(turns)
        lines.append(" ".join(str(faces[i][p[k]]) for k in range(6)))
    count = len(cells)
    m = rng.randint(1, 20) if mode == 1 else QUESTIONS
    questions = []
    # where each corner of the cube went in the shuffled order
    corners = [k + 1 for k, i in enumerate(order) if all(v in (0, n - 1) for v in cells[i])]
    for _ in range(m):
        pool = corners if mode == 3 else range(1, count + 1)
        a, b = sorted(rng.sample(pool, 2))
        questions.append("%d %d" % (a, b))
    print(side, n)
    print("\n".join(lines))
    print(m)
    print("\n".join(questions))


def extended(seed, mode):
    """5: maximal diagonal, m=1; 6: local neighbours at n=30, l=1;
    7: interior-only queries at odd n=29; 8: one interior anchor at n=30;
    9: planar queries at n=17, with dense runes ending at 10^9.
    All modes use proper rotations and put corners after non-corners.
    """
    rng = random.Random(seed)
    n = {5: 30, 6: 30, 7: 29, 8: 30, 9: 17}[mode]
    side = 1 if mode in (6, 9) else 100
    cells = [(x, y, z) for x in range(n) for y in range(n) for z in range(n)]
    index = {c: i for i, c in enumerate(cells)}
    faces = [[0] * 6 for _ in cells]
    edge_count = 3 * n * n * (n - 1)
    if mode == 9:
        runes = list(range(RUNES - edge_count + 1, RUNES + 1))
        rng.shuffle(runes)
    else:
        runes = rng.sample(range(2, RUNES), edge_count - 2) + [1, RUNES]
    for c in cells:
        for delta, here, there in (((0, 1, 0), 1, 0), ((1, 0, 0), 2, 3),
                                    ((0, 0, 1), 4, 5)):
            other = tuple(c[k] + delta[k] for k in range(3))
            if other in index:
                rune = runes.pop()
                faces[index[c]][here] = rune
                faces[index[other]][there] = rune
    order = list(range(len(cells)))
    rng.shuffle(order)
    order.sort(key=lambda i: all(v in (0, n - 1) for v in cells[i]))
    if mode == 8:
        centre = index[(n // 2,) * 3]
        order.remove(centre)
        order.insert(0, centre)
    number = {cells[i]: k + 1 for k, i in enumerate(order)}
    turns = rotations()
    print(side, n)
    for i in order:
        turn = rng.choice(turns)
        print(*(faces[i][k] for k in turn))
    m = 1 if mode == 5 else QUESTIONS
    print(m)
    interior = [c for c in cells if all(0 < v < n - 1 for v in c)] if mode == 7 else []
    local_steps = [(dx, dy, dz) for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                   for dz in (-1, 0, 1) if (dx, dy, dz) != (0, 0, 0)]
    for _ in range(m):
        if mode == 5:
            a, b = (0, 0, 0), (n - 1,) * 3
        elif mode == 6:
            a = rng.choice(cells)
            while True:
                delta = rng.choice(local_steps)
                b = tuple(a[k] + delta[k] for k in range(3))
                if b in number:
                    break
        elif mode == 7:
            a, b = rng.sample(interior, 2)
        elif mode == 8:
            a = (n // 2,) * 3
            b = rng.choice(cells)
            while a == b:
                b = rng.choice(cells)
        else:
            x = rng.randrange(n)
            yz = rng.sample(range(n * n), 2)
            a, b = [(x, v // n, v % n) for v in yz]
        print(*sorted((number[a], number[b])))


main()
