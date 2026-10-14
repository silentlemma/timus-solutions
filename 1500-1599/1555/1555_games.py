import sys
from array import array

# results of a position for the first player
UNKNOWN, WIN, LOSE, DRAW = 0, 1, 2, 3
INF = 65535
SIDES = 4
DIRECTION = "8624"  # north, east, south, west as on a keypad
WALL_CHAR = "-|-|"
DR = (-1, 0, 1, 0)
DC = (0, 1, 0, -1)
# the moves in the order of the answer: M8 M6 M2 M4 M5 S8 S6 S2 S4 S5
PASS, SUICIDE = 4, 9


def main():
    lines = sys.stdin.read().split("\n")
    n = int(lines[0])
    cells = n * n
    board = [lines[1 + i].rstrip("\r").ljust(3 * n) for i in range(3 * n)]
    side = [[-1] * SIDES for _ in range(cells)]
    step = [[-1] * SIDES for _ in range(cells)]
    walls = 0
    start1 = start2 = chest = -1
    for r in range(n):
        for c in range(n):
            cell = r * n + c
            mid = board[3 * r + 1][3 * c + 1]
            if mid == "1":
                start1 = cell
            elif mid == "2":
                start2 = cell
            elif mid == "*":
                chest = cell
            at = (board[3 * r][3 * c + 1], board[3 * r + 1][3 * c + 2],
                  board[3 * r + 2][3 * c + 1], board[3 * r + 1][3 * c])
            for d in range(SIDES):
                if at[d] == WALL_CHAR[d]:
                    side[cell][d] = walls
                    walls += 1
                nr, nc = r + DR[d], c + DC[d]
                if 0 <= nr < n and 0 <= nc < n:
                    step[cell][d] = nr * n + nc

    places = cells * cells * 6

    def place_id(a, b, h, turn):
        return ((a * cells + b) * 3 + h) * 2 + turn

    valid = [place_id(a, b, h, t) for a in range(cells) for b in range(cells)
             if a != b for h in range(3) for t in range(2)]

    def geometry(gone):
        """Steps through no standing wall and the flights of rockets."""
        def stands(w):
            return w >= 0 and w not in gone

        open_step = [-1] * (cells * SIDES)  # the cell a step leads to
        exit_ok = [False] * (cells * SIDES)  # a step out of the maze
        flight = [None] * (cells * SIDES)  # (cells on the way, wall hit or -1)
        for c in range(cells):
            for d in range(SIDES):
                nxt = step[c][d]
                back = (d + 2) % SIDES
                if nxt < 0:
                    exit_ok[c * SIDES + d] = not stands(side[c][d])
                elif not stands(side[c][d]) and not stands(side[nxt][back]):
                    open_step[c * SIDES + d] = nxt
                path = []
                pos, hit = c, -1
                while True:
                    if stands(side[pos][d]):
                        hit = side[pos][d]
                        break
                    nxt = step[pos][d]
                    if nxt < 0:
                        break
                    if stands(side[nxt][back]):
                        hit = side[nxt][back]
                        break
                    pos = nxt
                    path.append(pos)
                flight[c * SIDES + d] = (frozenset(path), hit)
        return open_step, exit_ok, flight

    # Moves that do not depend on the walls: a step is (side, next place), the side
    # being open or not by the rocket state; a pass goes through an extra side that
    # is always open. The same pairs, reversed, lead to the predecessors.
    passing = cells * SIDES
    steps = [None] * places
    preds = [[] for _ in range(places)]
    exits = [()] * places  # sides through which the mover may leave with the chest
    mover = [0] * places  # the cell of the player to move
    target = [0] * places  # the cell of the other player
    # the side between them if they are neighbours, else one never open
    blocked = [passing + 1] * places
    for p in valid:
        turn = p & 1
        h = (p >> 1) % 3
        a, b = divmod(p // 6, cells)
        cur, other = (a, b) if turn == 0 else (b, a)
        mover[p], target[p] = cur, other
        mine = turn + 1
        out = []
        ways = []
        for d in range(SIDES):
            nxt = step[cur][d]
            if nxt < 0:
                if h == mine:
                    out.append(cur * SIDES + d)
                continue
            if nxt == other:
                blocked[p] = cur * SIDES + d
                continue
            nh = mine if h == 0 and nxt == chest else h
            to = (((nxt * cells + b) * 3 + nh) << 1 | 1) if turn == 0 else \
                (((a * cells + nxt) * 3 + nh) << 1)
            ways.append((cur * SIDES + d, to))
        ways.append((passing, p ^ 1))
        steps[p] = ways
        for e, to in ways:
            preds[to].append((e, p))
        if out:
            exits[p] = tuple(out)

    # buffers of one rocket state, reused
    rest = [0] * places
    res = [0] * places
    seen = [0] * places
    dist = [INF] * places
    needed = [0] * places
    outside = [None] * places  # (result, turns) of the moves that leave the state

    def solve(loaded1, loaded2, gone, geo):
        open_step, exit_ok, flight = geo
        is_open = [x >= 0 for x in open_step] + [True, False]
        # open steps out of every cell, the pass included
        free = [1 + is_open[c * SIDES] + is_open[c * SIDES + 1] + is_open[c * SIDES + 2]
                + is_open[c * SIDES + 3] for c in range(cells)]
        # the states a shot leads to are solved first, since the buffers are shared
        later = ({}, {})
        for turn, loaded in ((0, loaded1), (1, loaded2)):
            if not loaded:
                continue
            for _, wall in flight:
                if wall not in later[turn]:
                    new_gone = gone | {wall} if wall >= 0 else gone
                    if turn == 0:
                        later[turn][wall] = state(False, loaded2, new_gone)
                    else:
                        later[turn][wall] = state(loaded1, False, new_gone)

        # the result by backward induction: a player wins as soon as one move
        # wins, loses when every move loses, and a cycle is a draw
        order = []
        for p in valid:
            turn = p & 1
            rest[p] = free[mover[p]] - is_open[blocked[p]]
            res[p] = UNKNOWN
            out = None
            for e in exits[p]:
                if exit_ok[e]:
                    # with the chest out of the maze
                    if out is None:
                        out = []
                    out.append((WIN if turn == 0 else LOSE, 0))
            if loaded1 if turn == 0 else loaded2:
                if out is None:
                    out = []
                base = mover[p] * SIDES
                other = target[p]
                tables = later[turn]
                for d in range(SIDES):
                    path, wall = flight[base + d]
                    if other in path:
                        out.append((WIN if turn == 0 else LOSE, 0))
                    else:
                        tres, tdist = tables[wall]
                        out.append((tres[p ^ 1], tdist[p ^ 1]))
                out.append((LOSE if turn == 0 else WIN, 0))
            outside[p] = out
            s = 0
            if out is not None:
                for r, _ in out:
                    s |= 1 << (r - 1)
                if turn == 0:
                    if s & 1:
                        res[p] = WIN
                        order.append(p)
                elif s & 2:
                    res[p] = LOSE
                    order.append(p)
            seen[p] = s
        head = 0
        while head < len(order):
            u = order[head]
            head += 1
            bit = 1 << (res[u] - 1)
            for e, q in preds[u]:
                if not is_open[e] or res[q] != UNKNOWN:
                    continue
                left = rest[q] - 1
                rest[q] = left
                s = seen[q] | bit
                seen[q] = s
                if q & 1 == 0:
                    if s & 1:
                        res[q] = WIN
                    elif left == 0:
                        res[q] = DRAW if s & 4 else LOSE
                    else:
                        continue
                else:
                    if s & 2:
                        res[q] = LOSE
                    elif left == 0:
                        res[q] = DRAW if s & 4 else WIN
                    else:
                        continue
                order.append(q)

        # Turns: the first player takes the fewest, the second the most, among moves
        # that keep the result. Turns only grow, so buckets serve as the queue, shared by
        # won and lost places; a losing second player has only moves that keep it.
        buckets = [[]]
        for p in valid:
            r = res[p]
            dist[p] = INF
            if r == UNKNOWN:
                res[p] = DRAW
                continue
            if r == DRAW:
                continue
            out = outside[p]
            if p & 1:
                if r == WIN:
                    need = free[mover[p]] - is_open[blocked[p]]
                    if out is not None:
                        need += len(out)
                else:
                    need = 0
                    for e, to in steps[p]:
                        if is_open[e] and res[to] == LOSE:
                            need += 1
                    if out is not None:
                        for x, _ in out:
                            if x == LOSE:
                                need += 1
                needed[p] = need
            if out is not None:
                for x, t in out:
                    if x == r and t < INF:
                        while len(buckets) <= t + 1:
                            buckets.append([])
                        buckets[t + 1].append(p)
        d = 0
        while d < len(buckets):
            for p in buckets[d]:
                if p & 1 == 0:
                    if dist[p] != INF:
                        continue
                else:
                    left = needed[p] - 1
                    needed[p] = left
                    if left:
                        continue
                dist[p] = d
                r = res[p]
                if len(buckets) == d + 1:
                    buckets.append([])
                nxt = buckets[d + 1]
                for e, q in preds[p]:
                    if is_open[e] and res[q] == r:
                        nxt.append(q)
            d += 1
        return bytearray(res), array("H", dist)

    # A rocket state is (first loaded, second loaded, destroyed walls), so equal
    # states are solved once; without rockets only the steps and the exits
    # matter, and states with the same ones share a table.
    by_walls = {}
    by_moves = {}

    def state(loaded1, loaded2, gone):
        key = (loaded1, loaded2, gone)
        table = by_walls.get(key)
        if table is None:
            geo = geometry(gone)
            if loaded1 or loaded2:
                table = solve(loaded1, loaded2, gone, geo)
            else:
                moves = (tuple(geo[0]), tuple(geo[1]))
                table = by_moves.get(moves)
                if table is None:
                    table = by_moves[moves] = solve(False, False, gone, geo)
            by_walls[key] = table
        return table

    tres, tdist = state(True, True, frozenset())
    start = place_id(start1, start2, 0, 0)
    result = tres[start]
    if result == DRAW:
        print("Draw")
        return

    # the first move: the best result, then the fewest turns, then the order of the moves
    open_step, exit_ok, flight = geometry(frozenset())
    options = []
    for d in range(SIDES):
        nxt = open_step[start1 * SIDES + d]
        if nxt < 0:
            continue  # the first player has no chest yet
        if nxt == start2:
            continue
        nh = 1 if nxt == chest else 0
        to = place_id(nxt, start2, nh, 1)
        options.append((d, tres[to], tdist[to]))
    options.append((PASS, tres[start ^ 1], tdist[start ^ 1]))
    for d in range(SIDES):
        path, wall = flight[start1 * SIDES + d]
        if start2 in path:
            options.append((PASS + 1 + d, WIN, 0))
        else:
            gone = frozenset([wall]) if wall >= 0 else frozenset()
            sres, sdist = state(False, True, gone)
            options.append((PASS + 1 + d, sres[start ^ 1], sdist[start ^ 1]))
    options.append((SUICIDE, LOSE, 0))
    strength = {WIN: 2, DRAW: 1, LOSE: 0}
    best = None
    for code, r, later_turns in options:
        if r == DRAW:
            turns = 0
        elif later_turns == INF:
            turns = INF
        else:
            turns = later_turns + 1
        if (best is None or strength[r] > strength[best[1]]
                or (strength[r] == strength[best[1]] and r != DRAW and turns < best[2])):
            best = (code, r, turns)
    code = best[0]
    print("%s %d" % ("Win" if result == WIN else "Lose", tdist[start]))
    print("%s%s" % ("M" if code <= PASS else "S",
                    "5" if code in (PASS, SUICIDE) else DIRECTION[code % (PASS + 1)]))


main()
