import sys
import time

# A mask is a set of grid cells, one bit each (grid <= 8 x 8).
SIDES = 4
MAXCELLS = 64
NONE = -1
INF = 1000000
TIME_LIMIT = 4.6  # seconds of search before giving up
DR = (-1, 1, 0, 0)
DC = (0, 0, -1, 1)
STEP = "udlr"
OPP = (1, 0, 3, 2)
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
PULLED = 1 << 63
WEIGHT = 3
BUCKETS = 4096
PUSH_ROUNDS = 8  # expansions of each search per round
PULL_ROUNDS = 1
CLOCK_EVERY = 128
MOST = 4
NEAR = 3  # sets of four only with boxes this close to the moved one


def low(x):
    return (x & -x).bit_length() - 1


def cells_of(m):
    out = []
    while m:
        b = m & -m
        out.append(b.bit_length() - 1)
        m ^= b
    return out


def main():
    started = time.time()
    lines = [line.rstrip("\r\n ") for line in sys.stdin.read().split("\n")]
    # drop the empty rows and columns around the level
    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.pop(0)
    lead = min(len(line) - len(line.lstrip(" ")) for line in lines if line)
    lines = [line[lead:] for line in lines]
    rows = len(lines)
    cols = max(len(line) for line in lines)
    cells = rows * cols
    walls = goals = start_boxes = 0
    start_player = 0
    for r in range(rows):
        for c in range(len(lines[r])):
            ch = lines[r][c]
            i = r * cols + c
            if ch == "#":
                walls |= 1 << i
            if ch in ".+*":
                goals |= 1 << i
            if ch in "$*":
                start_boxes |= 1 << i
            if ch in "@+":
                start_player = i
    nb = [[NONE] * cells for _ in range(SIDES)]
    not_first_col = not_last_col = 0
    for i in range(cells):
        for d in range(SIDES):
            r, c = i // cols + DR[d], i % cols + DC[d]
            if 0 <= r < rows and 0 <= c < cols:
                nb[d][i] = r * cols + c
        if i % cols:
            not_first_col |= 1 << i
        if i % cols != cols - 1:
            not_last_col |= 1 << i
    everything = (1 << cells) - 1

    # the player's area: the floor reachable from p around the boxes, as bit-parallel growth
    def flood(r, within):
        while True:
            x = (
                r
                | ((r << 1) & not_first_col)
                | ((r >> 1) & not_last_col)
                | (r << cols)
                | (r >> cols)
            ) & within
            if x == r:
                return r
            r = x

    def grow(r):
        return (
            r | ((r << 1) & not_first_col) | ((r >> 1) & not_last_col) | (r << cols) | (r >> cols)
        ) & everything

    # the floor: the cells the player reaches through non-walls; boxes on
    # goals walled off from the player never move and count as walls
    floor = flood(1 << start_player, everything & ~walls)
    goals &= floor
    start_boxes &= floor
    floor_cell = cells_of(floor)
    floor_index = [0] * cells
    for k, c in enumerate(floor_cell):
        floor_index[c] = k
    floor_count = len(floor_cell)
    box_bits = (1 << floor_count) - 1
    floor_bit = [1 << floor_index[c] for c in range(cells)]
    goal_count = bin(goals).count("1")

    def reach(p, boxes):
        return flood(1 << p, floor & ~boxes)

    # a state: a bit per floor cell for the boxes, then the floor index of the
    # lowest cell of the player's area
    def pack_key(boxes, player):
        k = 0
        while boxes:
            b = boxes & -boxes
            k |= floor_bit[b.bit_length() - 1]
            boxes ^= b
        return k | floor_index[player] << floor_count

    def key_boxes(key):
        b = 0
        k = key & box_bits
        while k:
            x = k & -k
            b |= 1 << floor_cell[x.bit_length() - 1]
            k ^= x
        return b

    def key_player(key):
        return floor_cell[(key & ~PULLED) >> floor_count]

    # push distances of a lone box: dist[target][cell] to bring a box from
    # cell to the target (pull False), or from the target to cell (pull True)
    def box_distances(targets, pull):
        unreachable = floor
        dist = []
        for target in cells_of(targets):
            dd = [INF] * cells
            dd[target] = 0
            queue = [target]
            for x in queue:
                unreachable &= ~(1 << x)
                for d in range(SIDES):
                    # a box pushed from y to x (the player behind y), or from x to y
                    if pull:
                        y, p = nb[d][x], nb[OPP[d]][x]
                    else:
                        y = nb[OPP[d]][x]
                        p = NONE if y < 0 else nb[OPP[d]][y]
                    if (
                        y < 0
                        or p < 0
                        or not (floor >> y) & 1
                        or not (floor >> p) & 1
                        or dd[y] != INF
                    ):
                        continue
                    dd[y] = dd[x] + 1
                    queue.append(y)
            dist.append(dd)
        return unreachable, dist

    dead, dist_push = box_distances(goals, False)
    dead_pull, dist_pull = box_distances(start_boxes, True)
    can_reach, nearest = [], []
    for dist in (dist_push, dist_pull):
        can_reach.append(
            [sum(1 << j for j in range(goal_count) if dist[j][c] < INF) for c in range(cells)]
        )
        nearest.append([min([dist[j][c] for j in range(goal_count)] + [INF]) for c in range(cells)])

    # A box is frozen when it can move along neither axis: a wall or a frozen
    # box on either side, or dead squares on both sides. Boxes already found
    # frozen count as walls while their neighbours are checked.
    state = {"as_wall": 0, "off_goal": False}

    def wall_like(c):
        return c < 0 or not (floor >> c) & 1 or (state["as_wall"] >> c) & 1

    def axis_blocked(x, d1, d2, boxes):
        a, b = nb[d1][x], nb[d2][x]
        if wall_like(a) or wall_like(b):
            return True
        if (dead >> a) & 1 and (dead >> b) & 1:
            return True
        return ((boxes >> a) & 1 and frozen(a, boxes)) or ((boxes >> b) & 1 and frozen(b, boxes))

    def frozen(x, boxes):
        saved = state["as_wall"]
        state["as_wall"] |= 1 << x
        f = axis_blocked(x, LEFT, RIGHT, boxes) and axis_blocked(x, UP, DOWN, boxes)
        state["as_wall"] = saved
        if f and not (goals >> x) & 1:
            state["off_goal"] = True
        return f

    # the box just pushed to x froze a box that is not on a goal
    def freeze_deadlock(x, boxes):
        state["as_wall"] = 0
        state["off_goal"] = False
        return frozen(x, boxes) and state["off_goal"]

    # h: the sum of each box's push distance to its nearest target; boxes that
    # cannot be matched to distinct reachable targets mean a deadlock
    def heuristic(boxes, way):
        targets = []
        h = 0
        near_way, reach_way = nearest[way], can_reach[way]
        for b in cells_of(boxes):
            h += near_way[b]
            targets.append(reach_way[b])
        match = [NONE] * goal_count

        def augment(i, seen):
            m = targets[i] & ~seen[0]
            while m:
                j = low(m)
                seen[0] |= 1 << j
                if match[j] < 0 or augment(match[j], seen):
                    match[j] = i
                    return True
                m &= m - 1
            return False

        for i in range(len(targets)):
            if not augment(i, [0]):
                return NONE
        return h

    # The pushes worth trying, or a deadlock. If every push of the boxes around
    # a region the player cannot reach goes inward and can be made now, one of
    # them is needed first, so only those are tried.
    def generate_pushes(boxes, area):
        out = []
        box_list = cells_of(boxes)
        for b in box_list:
            for d in range(SIDES):
                s, t = nb[OPP[d]][b], nb[d][b]
                if (
                    s >= 0
                    and t >= 0
                    and (area >> s) & 1
                    and (floor >> t) & 1
                    and not (boxes >> t) & 1
                ):
                    out.append((b, d))
        open_floor = floor & ~boxes & ~area
        unreached = open_floor
        best = None
        while unreached:
            corral = flood(unreached & -unreached, open_floor)
            unreached &= ~corral
            barrier = grow(corral) & boxes
            if not corral & goals and not barrier & ~goals:
                continue  # finished corral
            inward = ready = True
            candidates = []
            for b in cells_of(barrier):
                for d in range(SIDES):
                    s, t = nb[OPP[d]][b], nb[d][b]
                    # the player stands outside the corral and off the barrier
                    if s < 0 or not (floor >> s) & 1 or (corral >> s) & 1 or (barrier >> s) & 1:
                        continue
                    if t < 0 or not (floor >> t) & 1 or (barrier >> t) & 1:
                        continue  # blocked for good
                    if not (corral >> t) & 1:
                        inward = False  # a push away from the corral
                        break
                    if (area >> s) & 1:
                        candidates.append((b, d))
                    else:
                        ready = False
                if not inward:
                    break
            if not inward:
                continue
            if ready and not candidates:
                return None  # unfinished, and no push can ever enter it
            if ready and (best is None or len(candidates) < len(best)):
                best = candidates
        if best is not None and len(best) <= len(out):
            return best
        return out

    # For sets of k = 2..MOST cells, the player cells from which these boxes alone
    # can be solved (a pull search from the goals) or reached (a push search from
    # the start); a state with a failing subset is dead.

    set_table = [{}, {}]  # [solvable or reachable]: box set -> player cells

    def build_set_table(way, k):
        table = set_table[way]
        seen = set()
        queue = []
        sources = cells_of(start_boxes if way else goals)

        def combos(first, left, acc):
            if not left:
                yield acc
                return
            for i in range(first, len(sources) - left + 1):
                yield from combos(i + 1, left - 1, acc | 1 << sources[i])

        for chosen in combos(0, k, 0):  # every k of the start boxes or the goals
            if way:  # the player where it starts
                areas = [reach(start_player, chosen)]
            else:  # the player in any free area
                areas = []
                rest = floor & ~chosen
                while rest:
                    a = reach(low(rest), chosen)
                    rest &= ~a
                    areas.append(a)
            for a in areas:
                key = (chosen, low(a))
                if key not in seen:
                    seen.add(key)
                    queue.append(key)
        for boxes, player in queue:
            area = reach(player, boxes)
            table[boxes] = table.get(boxes, 0) | area
            for b in cells_of(boxes):
                rest = boxes & ~(1 << b)
                for d in range(SIDES):
                    x = nb[OPP[d]][b]
                    if x < 0 or not (area >> x) & 1:
                        continue
                    # a push from x moves the box to y; a pull to x moves the player to y
                    if way:
                        y = to = dest = nb[d][b]
                        to = b
                    else:
                        y = to = nb[OPP[d]][x]
                        dest = x
                    if y < 0 or not (floor >> y) & 1 or (boxes >> y) & 1:
                        continue
                    moved = rest | 1 << dest
                    key = (moved, low(reach(to, moved)))
                    if key not in seen:
                        seen.add(key)
                        queue.append(key)

    for k in range(2, min(MOST, goal_count) + 1):
        for way in range(2):
            build_set_table(way, k)

    # every set of up to MOST boxes with the moved box t is in the table
    def sets_ok(way, boxes, t, player):
        table = set_table[way]
        bt = 1 << t
        other = cells_of(boxes & ~bt)
        tr, tc = divmod(t, cols)
        close = [c for c in other if abs(c // cols - tr) <= NEAR and abs(c % cols - tc) <= NEAR]
        bits = [1 << c for c in other]
        for i, a in enumerate(bits):
            if not (table.get(bt | a, 0) >> player) & 1:
                return False
        for i, a in enumerate(bits):
            for b in bits[i + 1 :]:
                if not (table.get(bt | a | b, 0) >> player) & 1:
                    return False
        near_bits = [1 << c for c in close]
        n = len(near_bits)
        for i in range(n):
            for j in range(i + 1, n):
                for m in range(j + 1, n):
                    if (
                        not (
                            table.get(bt | near_bits[i] | near_bits[j] | near_bits[m], 0) >> player
                        )
                        & 1
                    ):
                        return False
        return True

    # Both searches share one dictionary from state key to the move that made it
    # (box floor index * 4 + direction, None for a start); pull-search keys
    # carry PULLED. Open lists are buckets by f = g + WEIGHT * h, each a stack.
    came = {}
    open_lists = ([[] for _ in range(BUCKETS)], [[] for _ in range(BUCKETS)])
    lowest = [BUCKETS, BUCKETS]

    def push_open(way, key, g, f):
        f = min(f, BUCKETS - 1)
        open_lists[way][f].append((key, g))
        if f < lowest[way]:
            lowest[way] = f

    def pop_open(way):
        buckets = open_lists[way]
        while lowest[way] < BUCKETS and not buckets[lowest[way]]:
            lowest[way] += 1
        if lowest[way] >= BUCKETS:
            return None
        return buckets[lowest[way]].pop()

    def expand_push(key, g):
        g += 1
        boxes = key_boxes(key)
        area = reach(key_player(key), boxes)
        pushes = generate_pushes(boxes, area)
        if pushes is None:
            return 0
        for b, d in pushes:
            t = nb[d][b]
            if (dead >> t) & 1:
                continue
            moved = (boxes & ~(1 << b)) | 1 << t
            if freeze_deadlock(t, moved):
                continue
            nxt = pack_key(moved, low(reach(b, moved)))
            if nxt in came or not sets_ok(0, moved, t, b):
                continue
            came[nxt] = floor_index[b] * SIDES + d
            if moved == goals or nxt | PULLED in came:
                return nxt
            h = heuristic(moved, 0)
            if h != NONE:  # a deadlocked state stays in the table as visited
                push_open(0, nxt, g, g + WEIGHT * h)
        return 0

    def expand_pull(key, g):
        g += 1
        boxes = key_boxes(key)
        area = reach(key_player(key), boxes)
        for b in cells_of(boxes):
            for d in range(SIDES):
                # the player at x pulls the box from b to x and steps back to y
                x = nb[OPP[d]][b]
                if x < 0 or not (area >> x) & 1 or (dead_pull >> x) & 1:
                    continue
                y = nb[OPP[d]][x]
                if y < 0 or not (floor >> y) & 1 or (boxes >> y) & 1:
                    continue
                moved = (boxes & ~(1 << b)) | 1 << x
                nxt = pack_key(moved, low(reach(y, moved)))
                if nxt | PULLED in came or not sets_ok(1, moved, x, y):
                    continue
                came[nxt | PULLED] = floor_index[x] * SIDES + d
                if nxt in came:
                    return nxt
                h = heuristic(moved, 1)
                if h != NONE:
                    push_open(1, nxt | PULLED, g, g + WEIGHT * h)
        return 0

    # The push search from the start and the pull search from the goal take
    # turns until some state is in both.
    def solve():
        root = pack_key(start_boxes, low(reach(start_player, start_boxes)))
        came[root] = None
        h0 = heuristic(start_boxes, 0)
        if h0 != NONE:
            push_open(0, root, 0, WEIGHT * h0)
        hg = heuristic(goals, 1)
        rest = floor & ~goals
        while rest:  # the boxes on the goals, the player anywhere
            area = reach(low(rest), goals)
            rest &= ~area
            key = pack_key(goals, low(area))
            if key | PULLED in came:
                continue
            came[key | PULLED] = None
            if key == root:
                return key
            if hg != NONE:
                push_open(1, key | PULLED, 0, WEIGHT * hg)
        rounds = 0
        while True:
            if rounds % CLOCK_EVERY == 0 and time.time() - started > TIME_LIMIT:
                return 0
            rounds += 1
            progress = False
            for _ in range(PUSH_ROUNDS):
                item = pop_open(0)
                if item is None:
                    break
                progress = True
                k = expand_push(*item)
                if k:
                    return k
            for _ in range(PULL_ROUNDS):
                item = pop_open(1)
                if item is None:
                    break
                progress = True
                k = expand_pull(*item)
                if k:
                    return k
            if not progress:
                return 0

    def walk(src, dst, boxes):
        if src == dst:
            return ""
        prev = {src: None}
        queue = [src]
        for x in queue:
            if x == dst:
                break
            for d in range(SIDES):
                y = nb[d][x]
                if y < 0 or not (floor >> y) & 1 or (boxes >> y) & 1 or y in prev:
                    continue
                prev[y] = (x, d)
                queue.append(y)
        steps = []
        x = dst
        while x != src:
            x, d = prev[x]
            steps.append(STEP[d])
        return "".join(reversed(steps))

    # the plan through the state key, which both searches reached (or which is solved)
    def build_answer(key):
        pushes = []
        k = key
        while came[k] is not None:  # back from key to the start through the push search
            move = came[k]
            b, d = floor_cell[move // SIDES], move % SIDES
            t = nb[d][b]
            pushes.append((b, d))
            boxes = (key_boxes(k) & ~(1 << t)) | 1 << b
            k = pack_key(boxes, low(reach(nb[OPP[d]][b], boxes)))
        pushes.reverse()
        if key_boxes(key) != goals:
            k = key
            while came[k | PULLED] is not None:  # forward to the goal: each pull, undone, is a push
                move = came[k | PULLED]
                x, d = floor_cell[move // SIDES], move % SIDES
                b = nb[d][x]
                pushes.append((x, d))
                boxes = (key_boxes(k) & ~(1 << x)) | 1 << b
                k = pack_key(boxes, low(reach(x, boxes)))
        out = []
        boxes = start_boxes
        pos = start_player
        for b, d in pushes:
            out.append(walk(pos, nb[OPP[d]][b], boxes))
            out.append(STEP[d].upper())
            boxes = (boxes & ~(1 << b)) | 1 << nb[d][b]
            pos = b
        return "".join(out)

    answer = ""
    if start_boxes != goals:
        meet = solve()
        if meet:
            answer = build_answer(meet)
    print(answer)


main()
