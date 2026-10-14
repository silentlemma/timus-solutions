"""A solvable level from a seed and a mode: walls around a room of up to
8 x 8 cells with some walls inside, the boxes put on the goals and then
pulled back by random moves of the player, so that pushing them back
solves the level. Mode 1 is a small room with one or two boxes, mode 2 an
8 x 8 room with five boxes, mode 3 a narrow room full of inner walls with
three boxes, mode 4 an open 8 x 8 room with six boxes, mode 5 a room of
random size, mode 6 an 8 x 8 room crowded with eight to eleven boxes,
mode 7 an 8 x 8 room with many inner walls and six to eight boxes."""

import random
import sys

STEPS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
LARGEST = 8
WALKS = 20000  # random moves of the player when scattering the boxes


def level(rng, rows, cols, inner, count):
    wall = [[r in (0, rows - 1) or c in (0, cols - 1) for c in range(cols)] for r in range(rows)]
    inside = [(r, c) for r in range(1, rows - 1) for c in range(1, cols - 1)]
    if len(inside) < count + 2:
        return None
    for r, c in rng.sample(inside, min(inner, len(inside) - count - 1)):
        wall[r][c] = True
    free = [(r, c) for r, c in inside if not wall[r][c]]
    # keep only the part connected to the first free cell
    seen, todo = {free[0]}, [free[0]]
    while todo:
        r, c = todo.pop()
        for dr, dc in STEPS:
            x = (r + dr, c + dc)
            if not wall[x[0]][x[1]] and x not in seen:
                seen.add(x)
                todo.append(x)
    for r, c in free:
        if (r, c) not in seen:
            wall[r][c] = True
    free = sorted(seen)
    if len(free) < count + 1:
        return None
    goals = set(rng.sample(free, count))
    boxes = set(goals)
    player = rng.choice([x for x in free if x not in boxes])
    for _ in range(WALKS):
        dr, dc = rng.choice(STEPS)
        to = (player[0] + dr, player[1] + dc)
        if wall[to[0]][to[1]] or to in boxes:
            continue
        behind = (player[0] - dr, player[1] - dc)
        if behind in boxes and rng.random() < 0.9:  # pull the box behind along
            boxes.remove(behind)
            boxes.add(player)
        player = to
    if boxes == goals:
        return None
    out = []
    for r in range(rows):
        line = ""
        for c in range(cols):
            x = (r, c)
            if wall[r][c]:
                line += "#"
            elif x == player:
                line += "+" if x in goals else "@"
            elif x in boxes:
                line += "*" if x in goals else "$"
            else:
                line += "." if x in goals else " "
        out.append(line)
    return out


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            made = level(rng, rng.randint(4, 6), rng.randint(4, 6), rng.randint(0, 3), rng.randint(1, 2))
        elif mode == 2:
            made = level(rng, LARGEST, LARGEST, rng.randint(3, 8), 5)
        elif mode == 3:
            made = level(rng, LARGEST, rng.randint(5, 6), rng.randint(6, 10), 3)
        elif mode == 4:
            made = level(rng, LARGEST, LARGEST, 0, 6)
        elif mode == 6:
            made = level(rng, LARGEST, LARGEST, rng.randint(0, 4), rng.randint(8, 11))
        elif mode == 7:
            made = level(rng, LARGEST, LARGEST, rng.randint(6, 12), rng.randint(6, 8))
        else:
            rows, cols = rng.randint(3, LARGEST), rng.randint(3, LARGEST)
            made = level(rng, rows, cols, rng.randint(0, 6), rng.randint(1, 4))
        if made:
            print("\n".join(made))
            return


main()
