"""A cut cube and questions from a seed and a mode: mode 1 a small cube,
2 the largest cube with the most questions, 3 the largest cube with
questions about far corners, 4 a cube of side 3 with the largest
crystals. Every contact gets its own random rune, every crystal a random
turn, and the crystals come in random order."""

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


main()
