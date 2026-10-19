"""Rabbits and a shot generator from a seed and a mode: mode 1 a few
rabbits near the origin and a few shots, 2 the most rabbits at random
and the most shots, 3 the most rabbits on a dense grid, so that many lie
on one line, 4 the most rabbits on a grid with a hunter standing still
in its middle and turning, 5 every rabbit on one diagonal, 6 rabbits
far from every shot, so that no shot hits and the last one is the
answer, 7 the most rabbits on a horizontal ray in a single shot,
8 one rabbit and the most shots with a hit on the final shot after
many position wraps, 9 random rabbits planted on generated rays plus
random distractors. The generator never yields a zero direction among
the shots."""

import random
import sys

MOST = 10000
SHOTS = 10 ** 6
SPAN = 10000
REACH = 10
LIMIT = 10 ** 5


def zero_free(start, a, b, q):
    vx, vy = start
    seen = set()
    for _ in range(q):
        if (vx, vy) == (0, 0):
            return False
        if (vx, vy) in seen:
            return True
        seen.add((vx, vy))
        vx = (a[0] * (vx + REACH) + b[0]) % (2 * REACH + 1) - REACH
        vy = (a[1] * (vy + REACH) + b[1]) % (2 * REACH + 1) - REACH
    return True


def extra_mode(rng, mode):
    if mode == 7:
        y = rng.randint(-SPAN, SPAN)
        rabbits = [(x, y) for x in range(-MOST // 2, MOST // 2)]
        q, first = 1, [-SPAN, y, REACH, 0]
        parameters = [0] * 8
    elif mode == 8:
        x, y = rng.randint(-SPAN, SPAN), rng.randint(-9000, -1000)
        q, first = SHOTS, [x, y, 0, rng.randint(1, REACH)]
        last_x = (x + SPAN + q - 1) % (2 * SPAN + 1) - SPAN
        rabbits = [(last_x, y + 1000)]
        parameters = [1, 1, 1, 0, 1, 0, 1, 0]
    else:
        q = rng.randint(50, 120)
        first = [rng.randint(-9000, 9000), rng.randint(-9000, 9000),
                 rng.randint(-REACH, REACH), rng.randint(-REACH, REACH)]
        while True:
            parameters = [rng.randint(0, LIMIT) for _ in range(8)]
            if zero_free(first[2:], (parameters[4], parameters[6]),
                         (parameters[5], parameters[7]), q):
                break
            first[2:] = [rng.randint(-REACH, REACH), rng.randint(-REACH, REACH)]
        states, state = [], first[:]
        for _ in range(q):
            states.append(state)
            state = [(parameters[2 * k] * (value + bound) + parameters[2 * k + 1])
                     % (2 * bound + 1) - bound
                     for k, (value, bound) in enumerate(zip(state, (SPAN, SPAN, REACH, REACH)))]
        points = set()
        for _ in range(3000):
            if len(points) == 150:
                break
            x, y, vx, vy = rng.choice(states)
            t = rng.randint(-20, 30)
            point = (x + t * vx, y + t * vy)
            if all(-SPAN <= value <= SPAN for value in point):
                points.add(point)
        while len(points) < 200:
            points.add((rng.randint(-SPAN, SPAN), rng.randint(-SPAN, SPAN)))
        rabbits = sorted(points)
    rng.shuffle(rabbits)
    print(len(rabbits))
    print("\n".join("%d %d" % r for r in rabbits))
    print(q)
    print(*first)
    print(*parameters)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (7, 8, 9):
        extra_mode(rng, mode)
        return
    rabbits = set()
    if mode == 1:
        size = rng.randint(1, 12)
        while len(rabbits) < size:
            rabbits.add((rng.randint(-4, 4), rng.randint(-4, 4)))
    elif mode in (3, 4):
        rabbits = {(x, y) for x in range(-50, 50) for y in range(-50, 50)}
    elif mode == 5:
        rabbits = {(t - MOST // 2, t - MOST // 2) for t in range(MOST)}
    elif mode == 6:
        while len(rabbits) < MOST:
            rabbits.add((rng.randint(SPAN - 200, SPAN), rng.randint(SPAN - 200, SPAN)))
    else:
        while len(rabbits) < MOST:
            rabbits.add((rng.randint(-SPAN, SPAN), rng.randint(-SPAN, SPAN)))
    q = rng.randint(1, 30) if mode == 1 else SHOTS
    while True:
        if mode == 1:
            hunter = [rng.randint(-5, 5), rng.randint(-5, 5)]
            moves = [rng.randint(0, 3), rng.randint(0, 3), rng.randint(0, 3), rng.randint(0, 3)]
        elif mode == 6:
            hunter = [-SPAN, -SPAN]
            moves = [1, 0, 1, 0]
        else:
            hunter = [rng.randint(-SPAN, SPAN), rng.randint(-SPAN, SPAN)]
            moves = [rng.randint(0, LIMIT) for _ in range(4)]
        if mode == 4:
            hunter, moves = [0, 0], [1, 0, 1, 0]
        turns = [rng.randint(0, LIMIT) for _ in range(4)]
        if mode == 6:
            # always pointing down and to the left, away from the rabbits
            turns = [1, 0, 1, 0]
            direction = [-rng.randint(1, REACH), -rng.randint(1, REACH)]
        else:
            direction = [rng.randint(-REACH, REACH), rng.randint(-REACH, REACH)]
        if zero_free(direction, (turns[0], turns[2]), (turns[1], turns[3]), q):
            break
    print(len(rabbits))
    print("\n".join("%d %d" % r for r in sorted(rabbits, key=lambda r: rng.random())))
    print(q)
    print(*(hunter + direction))
    print(moves[0], moves[1], moves[2], moves[3], turns[0], turns[1], turns[2], turns[3])


main()
