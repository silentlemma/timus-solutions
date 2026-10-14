import sys
from array import array
from itertools import combinations

# A mask is a set of grid cells, one bit each (grid <= 8 x 8).
SIDES = 4
MAXCELLS = 64
NONE = -1
INF = 1000000
DR = (-1, 1, 0, 0)
DC = (0, 0, -1, 1)
STEP = "udlr"
OPP = (1, 0, 3, 2)
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
MAX_SIDE = 8
PLAYER_BITS = 6
PLAYER_SHIFT = MAXCELLS - MAX_SIDE - 1
PULLED = 1 << (PLAYER_SHIFT + PLAYER_BITS)
WEIGHT = 3
BUCKETS = 4096
TABLE_BITS = 21
TABLE = 1 << TABLE_BITS
TABLE_MASK = TABLE - 1
TABLE_FILL = TABLE // 100 * 88
HASH_SHIFT = 31
HASH_MIX = 17
HASH_MASK = (1 << HASH_SHIFT) - 1
HASH_MULT = 1540483477
DEPTH_BITS = 16
DEPTH_MAX = (1 << DEPTH_BITS) - 1
ROOT = 255
PUSH_ROUNDS = 8  # expansions of each search per round
PULL_ROUNDS = 1
MOST = 4
TRIO = 3
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
    for i in range(cells):
        for d in range(SIDES):
            r, c = i // cols + DR[d], i % cols + DC[d]
            if 0 <= r < rows and 0 <= c < cols:
                nb[d][i] = r * cols + c
    everything = (1 << cells) - 1

    # Enclosing walls stop horizontal growth before it could wrap into another row.
    def flood(r, within):
        while True:
            x = (
                r
                | (r << 1)
                | (r >> 1)
                | (r << cols)
                | (r >> cols)
            ) & within
            if x == r:
                return r
            r = x

    def grow(r):
        return (
            r | (r << 1) | (r >> 1) | (r << cols) | (r >> cols)
        ) & everything

    # the floor: the cells the player reaches through non-walls; boxes on
    # goals walled off from the player never move and count as walls
    floor = flood(1 << start_player, everything & ~walls)
    goals &= floor
    start_boxes &= floor
    if start_boxes == goals:
        print("")
        return
    floor_cell = cells_of(floor)
    floor_index = [0] * cells
    for k, c in enumerate(floor_cell):
        floor_index[c] = k
    floor_count = len(floor_cell)
    goal_count = bin(goals).count("1")

    def reach(p, boxes):
        return flood(1 << p, floor & ~boxes)

    # Interior grid bits fit below the player field, so no board conversion is needed.
    def pack_key(boxes, player):
        return boxes | player << PLAYER_SHIFT

    def key_boxes(key):
        return key & floor

    def key_player(key):
        return (key & ~PULLED) >> PLAYER_SHIFT

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

    choose = [[0] * cells for _ in range(MOST + 1)]
    sizes = [1] * (MOST + 1)
    for k in range(1, MOST + 1):
        for c in floor_cell:
            n = floor_index[c]
            value = 1
            for j in range(k):
                value = value * (n - j) // (j + 1)
            choose[k][c] = value if n >= k else 0
        sizes[k] = sizes[k - 1] * (floor_count - k + 1) // k
    set_table = [[None] * (MOST + 1) for _ in range(2)]

    def set_index(boxes):
        index = 0
        rank = 1
        while boxes:
            b = boxes & -boxes
            index += choose[rank][b.bit_length() - 1]
            rank += 1
            boxes ^= b
        return index

    def build_set_table(way, k):
        table = array("Q", [0]) * sizes[k]
        set_table[way][k] = table
        queue = array("Q")

        def enqueue(boxes, seed):
            index = set_index(boxes)
            if table[index] & seed:
                return
            area = flood(seed, floor & ~boxes)
            table[index] |= area
            queue.append(boxes)
            queue.append(area)

        sources = cells_of(start_boxes if way else goals)
        for chosen in combinations(sources, k):
            boxes = sum(1 << c for c in chosen)
            if way:
                enqueue(boxes, 1 << start_player)
            else:
                rest = floor & ~boxes
                while rest:
                    area = flood(rest & -rest, rest)
                    enqueue(boxes, area & -area)
                    rest &= ~area
        head = 0
        shifts = (-cols, cols, -1, 1)
        while head < len(queue):
            boxes, area = queue[head], queue[head + 1]
            head += 2
            free = floor & ~boxes
            for delta in shifts:
                if way:
                    movable = boxes & (area << delta if delta > 0 else area >> -delta)
                    movable &= free >> delta if delta > 0 else free << -delta
                else:
                    ready = area & (free << delta if delta > 0 else free >> -delta)
                    movable = boxes & (ready << delta if delta > 0 else ready >> -delta)
                while movable:
                    b = movable & -movable
                    movable ^= b
                    if way:
                        dest = b << delta if delta > 0 else b >> -delta
                        seed = b
                    else:
                        dest = b >> delta if delta > 0 else b << -delta
                        seed = dest >> delta if delta > 0 else dest << -delta
                    enqueue(boxes ^ b ^ dest, seed)

    for k in range(2, min(MOST, goal_count) + 1):
        for way in range(2):
            build_set_table(way, k)

    def index2(a, x):
        if x < a:
            a, x = x, a
        return choose[1][a] + choose[2][x]

    def index3(a, b, x):
        if x < a:
            return choose[1][x] + choose[2][a] + choose[TRIO][b]
        if x < b:
            return choose[1][a] + choose[2][x] + choose[TRIO][b]
        return choose[1][a] + choose[2][b] + choose[TRIO][x]

    def index4(a, b, c, x):
        if x < a:
            return choose[1][x] + choose[2][a] + choose[TRIO][b] + choose[MOST][c]
        if x < b:
            return choose[1][a] + choose[2][x] + choose[TRIO][b] + choose[MOST][c]
        if x < c:
            return choose[1][a] + choose[2][b] + choose[TRIO][x] + choose[MOST][c]
        return choose[1][a] + choose[2][b] + choose[TRIO][c] + choose[MOST][x]

    # Only subsets containing the moved box can have become deadlocked.
    def sets_ok(way, boxes, t, player):
        pairs, trios, fours = set_table[way][2:]
        other = cells_of(boxes & ~(1 << t))
        pb = 1 << player
        for a in other:
            if not pairs[index2(a, t)] & pb:
                return False
        for i, a in enumerate(other):
            for b in other[i + 1:]:
                if not trios[index3(a, b, t)] & pb:
                    return False
        tr, tc = divmod(t, cols)
        close = [c for c in other if abs(c // cols - tr) <= NEAR and abs(c % cols - tc) <= NEAR]
        for i, a in enumerate(close):
            for j in range(i + 1, len(close)):
                for m in range(j + 1, len(close)):
                    if not fours[index4(a, close[j], close[m], t)] & pb:
                        return False
        return True

    # States and bucket links use primitive arrays; no tuple is kept per search node.
    table_keys = array("Q", [0]) * TABLE
    table_moves = bytearray(TABLE)
    table_next = array("I", [0]) * TABLE
    table_depth = array("H", [0]) * TABLE
    heads = array("I", [0]) * (2 * BUCKETS)
    lowest = [BUCKETS, BUCKETS]
    key_count = 0

    def probe(key):
        h = key ^ (key >> HASH_SHIFT)
        h ^= h >> HASH_MIX
        slot = ((h & HASH_MASK) * HASH_MULT) & TABLE_MASK
        while table_keys[slot]:
            if table_keys[slot] == key:
                return slot
            slot = (slot + 1) & TABLE_MASK
        return ~slot

    def insert(slot, key, move):
        nonlocal key_count
        if key_count >= TABLE_FILL:
            raise MemoryError("state table full")
        key_count += 1
        table_keys[slot] = key
        table_moves[slot] = move

    def push_open(way, slot, g, f):
        f = min(f, BUCKETS - 1)
        bucket = way * BUCKETS + f
        table_next[slot] = heads[bucket]
        table_depth[slot] = min(g, DEPTH_MAX)
        heads[bucket] = slot + 1
        if f < lowest[way]:
            lowest[way] = f

    def pop_open(way):
        base = way * BUCKETS
        f = lowest[way]
        while f < BUCKETS and not heads[base + f]:
            f += 1
        lowest[way] = f
        if f == BUCKETS:
            return 0
        item = heads[base + f]
        heads[base + f] = table_next[item - 1]
        return item

    def expand_push(slot):
        key = table_keys[slot]
        g = table_depth[slot] + 1
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
            slot = probe(nxt)
            if slot >= 0 or not sets_ok(0, moved, t, b):
                continue
            slot = ~slot
            insert(slot, nxt, floor_index[b] * SIDES + d)
            if moved == goals or probe(nxt | PULLED) >= 0:
                return nxt
            h = heuristic(moved, 0)
            if h != NONE:  # a deadlocked state stays in the table as visited
                push_open(0, slot, g, g + WEIGHT * h)
        return 0

    def expand_pull(slot):
        key = table_keys[slot]
        g = table_depth[slot] + 1
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
                slot = probe(nxt | PULLED)
                if slot >= 0 or not sets_ok(1, moved, x, y):
                    continue
                slot = ~slot
                insert(slot, nxt | PULLED, floor_index[x] * SIDES + d)
                if probe(nxt) >= 0:
                    return nxt
                h = heuristic(moved, 1)
                if h != NONE:
                    push_open(1, slot, g, g + WEIGHT * h)
        return 0

    # The push search from the start and the pull search from the goal take
    # turns until some state is in both.
    def solve():
        root = pack_key(start_boxes, low(reach(start_player, start_boxes)))
        slot = ~probe(root)
        insert(slot, root, ROOT)
        h0 = heuristic(start_boxes, 0)
        if h0 != NONE:
            push_open(0, slot, 0, WEIGHT * h0)
        hg = heuristic(goals, 1)
        rest = floor & ~goals
        while rest:  # the boxes on the goals, the player anywhere
            area = reach(low(rest), goals)
            rest &= ~area
            key = pack_key(goals, low(area))
            slot = probe(key | PULLED)
            if slot >= 0:
                continue
            slot = ~slot
            insert(slot, key | PULLED, ROOT)
            if key == root:
                return key
            if hg != NONE:
                push_open(1, slot, 0, WEIGHT * hg)
        while True:
            progress = False
            for _ in range(PUSH_ROUNDS):
                item = pop_open(0)
                if not item:
                    break
                progress = True
                k = expand_push(item - 1)
                if k:
                    return k
            for _ in range(PULL_ROUNDS):
                item = pop_open(1)
                if not item:
                    break
                progress = True
                k = expand_pull(item - 1)
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
        while table_moves[probe(k)] != ROOT:
            move = table_moves[probe(k)]
            b, d = floor_cell[move // SIDES], move % SIDES
            t = nb[d][b]
            pushes.append((b, d))
            boxes = (key_boxes(k) & ~(1 << t)) | 1 << b
            k = pack_key(boxes, low(reach(nb[OPP[d]][b], boxes)))
        pushes.reverse()
        if key_boxes(key) != goals:
            k = key
            while table_moves[probe(k | PULLED)] != ROOT:
                move = table_moves[probe(k | PULLED)]
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
