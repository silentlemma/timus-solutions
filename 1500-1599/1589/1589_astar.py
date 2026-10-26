"""Best-first push searches with regional deadlock tables, then subset tables."""

import heapq
import sys
from time import perf_counter

try:
    import pypyjit

    # a short run: compile less, and earlier, instead of optimizing harder
    pypyjit.set_param(
        "trace_limit=3000,enable_opts=intbounds:rewrite:virtualize:string:pure:earlyforce:heap"
    )
except ImportError:
    pass

BOARD_WIDTH = 8
DIRECTIONS = 4
BYTE_VALUES = 256
BYTE_MASK = BYTE_VALUES - 1
DISTANCE_RING = 128
DISTANCE_RING_MASK = DISTANCE_RING - 1
SYMMETRIES = 8
REFLECTION_FLAG = 4
ROTATION_MASK = 3
PLAYER_INDEX = 3
DIRECTION_PROBE_CELL = 27
CELL_COUNT = 64
PLAYER_SHIFT = 56
BOX_BITS = (1 << PLAYER_SHIFT) - 1
MAX_BOXES = 36
MAX_PLAN_LENGTH = 10000
UNREACHABLE = 10000
REGION_WIDTH = 3
SMALL_PATTERN_SIZE = 3
FOUR_BOX_PATTERN_SIZE = 4
LARGE_PATTERN_SIZE = 5
PRIORITY_SCALE = 100
PACKING_WEIGHT = 30
INITIAL_EXPANSIONS = 128
SMALL_BOX_EXPANSIONS = 4000
MANY_BOX_EXPANSIONS = 256
SMALL_BOX_COUNT = 10
UNBOUNDED = 1 << 62
NODE_CAP = 300000
FAST_SECONDS = 4.5
CLOCK_CHECK_MASK = 255
ID_BITS = 26
ID_SCALE = 1 << ID_BITS
NO_PARENT = -1
STEP = (-BOARD_WIDTH, BOARD_WIDTH, -1, 1)
LETTERS = "udlr"
STARTED = perf_counter()


class FailedWalk(Exception):
    pass


def shift(mask, direction):
    if direction == 0:
        return mask >> BOARD_WIDTH
    if direction == 1:
        return mask << BOARD_WIDTH
    if direction == 2:
        return mask >> 1
    return mask << 1


def reach(seed, free):
    while True:
        grown = (
            seed | (seed << BOARD_WIDTH) | (seed >> BOARD_WIDTH) | (seed << 1) | (seed >> 1)
        ) & free
        if grown == seed:
            return seed
        seed = grown


def low(mask):
    return (mask & -mask).bit_length() - 1


def bits(mask):
    return bin(mask).count("1")


def rotate_cell(cell):
    return (cell % BOARD_WIDTH) * BOARD_WIDTH + BOARD_WIDTH - 1 - cell // BOARD_WIDTH


# The level, possibly rotated or reflected, and the search state of an attempt.
floor = goal = start_boxes = live = targets = 0
start_player = 0
reverse = False
fast_mode = True
crossing_penalty = 0
use_regional = False
pattern_size = 0
packing_weight = 0
goals = []
node_state = []
node_parent = []
node_move = []
seen = {}
heuristic_cache = {}
distance_cache = {}
edge_cache = {}
packing = {}
regions = []
patterns = {}
moved_box = parent_frozen = 0
parent_dual = None
parent_boxes = 0
moved_from = moved_to = 0
binomial = [[0] * (LARGE_PATTERN_SIZE + 1) for _ in range(MAX_BOXES + 1)]
for _cells in range(MAX_BOXES + 1):
    for _size in range(LARGE_PATTERN_SIZE + 1):
        binomial[_cells][_size] = (
            1
            if _size == 0
            else 0
            if _cells == 0
            else binomial[_cells - 1][_size - 1] + binomial[_cells - 1][_size]
        )


def frozen_boxes(boxes):
    while True:
        previous = boxes
        empty = floor & ~boxes
        empty_live = empty & live
        if not reverse:
            removable = (
                (empty >> BOARD_WIDTH) & (empty_live << BOARD_WIDTH)
                | (empty << BOARD_WIDTH) & (empty_live >> BOARD_WIDTH)
                | (empty >> 1) & (empty_live << 1)
                | (empty << 1) & (empty_live >> 1)
            )
        else:
            removable = (
                ((empty & (empty << BOARD_WIDTH)) & live) << BOARD_WIDTH
                | ((empty & (empty >> BOARD_WIDTH)) & live) >> BOARD_WIDTH
                | ((empty & (empty << 1)) & live) << 1
                | ((empty & (empty >> 1)) & live) >> 1
            )
        boxes &= ~removable
        if boxes == previous:
            return boxes


def insert(state, parent, move):
    seen[state] = len(node_state)
    node_state.append(state)
    node_parent.append(parent)
    node_move.append(move)
    return len(node_state) - 1


def shortest_walk(boxes, player, destination):
    free = floor & ~boxes
    previous_cell = {player: player}
    previous_direction = {}
    queue = [player]
    head = 0
    while head < len(queue) and destination not in previous_cell:
        cell = queue[head]
        head += 1
        for direction in range(DIRECTIONS):
            next_cell = cell + STEP[direction]
            if (
                0 <= next_cell < CELL_COUNT
                and free >> next_cell & 1
                and next_cell not in previous_cell
            ):
                previous_cell[next_cell] = cell
                previous_direction[next_cell] = direction
                queue.append(next_cell)
    if destination not in previous_cell:
        raise FailedWalk
    walk = []
    cell = destination
    while cell != player:
        walk.append(LETTERS[previous_direction[cell]])
        cell = previous_cell[cell]
    walk.reverse()
    return "".join(walk)


def reconstruct(node):
    pushes = []
    while node_parent[node] != NO_PARENT:
        pushes.append(node_move[node])
        node = node_parent[node]
    if not reverse:
        pushes.reverse()
    boxes, player = start_boxes, start_player
    plan = []
    for encoded in pushes:
        cell, direction = divmod(encoded, DIRECTIONS)
        if reverse:
            cell += STEP[direction]
            direction ^= 1
        plan.append(shortest_walk(boxes, player, cell - STEP[direction]))
        plan.append(LETTERS[direction].upper())
        boxes ^= (1 << cell) | (1 << (cell + STEP[direction]))
        player = cell
    return "".join(plan)


def restrict_corral(boxes, reachable):
    unseen = floor & ~(boxes | reachable)
    fixed = frozen_boxes(boxes)
    while unseen:
        corral = reach(unseen & -unseen, floor & ~(boxes | reachable))
        unseen &= ~corral
        border = boxes & (
            (corral << 1) | (corral >> 1) | (corral << BOARD_WIDTH) | (corral >> BOARD_WIDTH)
        )
        if not ((border & ~goal) | (corral & goal)):
            continue
        reduced = border | fixed
        relaxed = reach(reachable, floor & ~reduced)
        independent = True
        push_count = 0
        for direction in range(DIRECTIONS):
            possible = (
                border & shift(relaxed, direction) & shift((floor & ~reduced) & live, direction ^ 1)
            )
            actual = (
                border & shift(reachable, direction) & shift((floor & ~boxes) & live, direction ^ 1)
            )
            if possible != actual or (shift(possible, direction) & ~corral):
                independent = False
                break
            push_count += bits(possible)
        if independent and push_count:
            return border
    return boxes


class Region:
    """Exact solvability of the boxes in a strip; boxes outside disappear."""

    def __init__(self, region_mask):
        region_floor = floor
        active = goal
        while True:
            previous = active
            for direction in range(DIRECTIONS):
                active |= (
                    shift(active, direction) & shift(region_floor, direction ^ 1) & region_floor
                )
            if active == previous:
                break
        region_mask &= active
        self.mask = region_mask
        cells = []
        remaining = region_mask
        while remaining:
            cells.append(low(remaining))
            remaining &= remaining - 1
        solvable = [0] * (1 << len(cells))
        self.rows = []
        self.packed = []
        for row in range(BOARD_WIDTH):
            masks = [0] * BOARD_WIDTH
            used = False
            for index, cell in enumerate(cells):
                if cell // BOARD_WIDTH == row:
                    masks[cell % BOARD_WIDTH] = 1 << index
                    used = True
            if not used:
                continue
            table = [0] * BYTE_VALUES
            for value in range(1, BYTE_VALUES):
                table[value] = table[value & (value - 1)] | masks[low(value)]
            self.rows.append(row * BOARD_WIDTH)
            self.packed.append(table)
        self.solvable = solvable
        # the subset index of the boxes changes by one or two bits per pull
        cell_bit = [0] * CELL_COUNT
        for index, cell in enumerate(cells):
            cell_bit[cell] = 1 << index
        queue_boxes, queue_index, queue_reach, queue_count = [], [], [], []

        def add(boxes, packed, count, seed):
            if solvable[packed] & seed:
                return
            reachable = reach(seed, region_floor & ~boxes)
            solvable[packed] |= reachable
            queue_boxes.append(boxes)
            queue_index.append(packed)
            queue_reach.append(reachable)
            queue_count.append(count)

        boxes = goal & region_mask
        packed = 0
        remaining = boxes
        while remaining:
            packed |= cell_bit[low(remaining)]
            remaining &= remaining - 1
        count = bits(boxes)
        todo = region_floor & ~boxes
        while todo:
            reachable = reach(todo & -todo, region_floor & ~boxes)
            add(boxes, packed, count, reachable)
            todo &= ~reachable
        outside = active & ~region_mask
        start_count = bits(start_boxes)
        head = 0
        while head < len(queue_boxes):
            boxes = queue_boxes[head]
            packed = queue_index[head]
            reachable = queue_reach[head]
            count = queue_count[head]
            head += 1
            empty = region_floor & ~boxes
            importing = count < start_count
            for direction in range(DIRECTIONS):
                step = STEP[direction]
                # boxes next to the player, with an empty cell behind the player
                if direction == 0:
                    behind = reachable & (empty << BOARD_WIDTH)
                    movable = boxes & ((behind & active) << BOARD_WIDTH)
                    behind_outside = (behind & region_mask) << BOARD_WIDTH
                elif direction == 1:
                    behind = reachable & (empty >> BOARD_WIDTH)
                    movable = boxes & ((behind & active) >> BOARD_WIDTH)
                    behind_outside = (behind & region_mask) >> BOARD_WIDTH
                elif direction == 2:
                    behind = reachable & (empty << 1)
                    movable = boxes & ((behind & active) << 1)
                    behind_outside = (behind & region_mask) << 1
                else:
                    behind = reachable & (empty >> 1)
                    movable = boxes & ((behind & active) >> 1)
                    behind_outside = (behind & region_mask) >> 1
                while movable:
                    cell = (movable & -movable).bit_length() - 1
                    movable &= movable - 1
                    next_cell = cell + step
                    next_bit = cell_bit[next_cell] if region_mask >> next_cell & 1 else 0
                    if next_bit:
                        add(
                            boxes ^ (1 << cell) | (1 << next_cell),
                            packed ^ cell_bit[cell] | next_bit,
                            count,
                            1 << (next_cell + step),
                        )
                    else:
                        add(
                            boxes ^ (1 << cell),
                            packed ^ cell_bit[cell],
                            count - 1,
                            1 << (next_cell + step),
                        )
                if importing:
                    movable = outside & behind_outside
                    while movable:
                        cell = (movable & -movable).bit_length() - 1
                        movable &= movable - 1
                        next_cell = cell + step
                        add(
                            boxes | (1 << next_cell),
                            packed | cell_bit[next_cell],
                            count + 1,
                            1 << (next_cell + step),
                        )

    def index(self, boxes):
        packed = 0
        for row, table in zip(self.rows, self.packed):
            packed |= table[(boxes >> row) & BYTE_MASK]
        return packed


def build_regions():
    for axis in range(2):
        for side in range(2):
            minimum, maximum = BOARD_WIDTH, 0
            remaining = floor
            while remaining:
                cell = low(remaining)
                remaining &= remaining - 1
                coordinate = cell // BOARD_WIDTH if axis else cell % BOARD_WIDTH
                minimum = min(minimum, coordinate)
                maximum = max(maximum, coordinate)
            region_mask = 0
            remaining = live
            while remaining:
                cell = low(remaining)
                remaining &= remaining - 1
                coordinate = cell // BOARD_WIDTH if axis else cell % BOARD_WIDTH
                if (
                    (coordinate > maximum - REGION_WIDTH)
                    if side
                    else (coordinate < minimum + REGION_WIDTH)
                ):
                    region_mask |= 1 << cell
            if not region_mask or any(region.mask == region_mask for region in regions):
                continue
            regions.append(Region(region_mask))


def region_good(boxes, reachable):
    if not regions:
        build_regions()
    for region in regions:
        if not region.solvable[region.index(boxes)] & reachable:
            return False
    return True


def inaccessible_boxes(boxes, reachable):
    while True:
        empty = floor & ~boxes
        if reverse:
            removable = boxes & (
                ((reachable & (empty << BOARD_WIDTH) & live) << BOARD_WIDTH)
                | ((reachable & (empty >> BOARD_WIDTH) & live) >> BOARD_WIDTH)
                | ((reachable & (empty << 1) & live) << 1)
                | ((reachable & (empty >> 1) & live) >> 1)
            )
        else:
            empty_live = empty & live
            removable = boxes & (
                ((reachable >> BOARD_WIDTH) & (empty_live << BOARD_WIDTH))
                | ((reachable << BOARD_WIDTH) & (empty_live >> BOARD_WIDTH))
                | ((reachable >> 1) & (empty_live << 1))
                | ((reachable << 1) & (empty_live >> 1))
            )
        if not removable:
            return boxes
        boxes &= ~removable
        reachable = reach(reachable, floor & ~boxes)


def packing_residues(fixed):
    results = packing.get(fixed)
    if results is None:
        results = []
        todo = floor & ~goal
        while todo:
            remaining = goal
            reachable = reach(todo & -todo, floor & ~goal)
            todo &= ~reachable
            while True:
                empty = floor & ~remaining
                movable = 0
                for direction in range(DIRECTIONS):
                    movable |= remaining & shift(
                        reachable & shift(empty, direction ^ 1), direction ^ 1
                    )
                movable &= ~fixed
                if not movable:
                    break
                remaining &= ~movable
                reachable = reach(reachable, floor & ~remaining)
            results.append((remaining, reachable))
        packing[fixed] = results
    return results


def packing_good(boxes, reachable, fixed):
    for remaining, region in packing_residues(fixed):
        if not (remaining & ~boxes) and (region & reachable):
            return True
    return False


class Pattern:
    """Solvable player components of every subset of a few boxes."""

    def __init__(self, fixed):
        self.floor = floor & ~fixed
        self.goals = targets & ~fixed
        self.size = min(pattern_size, bits(self.goals))
        self.cell_index = [-1] * CELL_COUNT
        self.live = 0
        self.solvable = []
        if self.size < 1:
            return
        pattern_floor = self.floor
        live_cells = self.goals
        while True:
            previous = live_cells
            for direction in range(DIRECTIONS):
                if reverse:
                    live_cells |= (
                        shift(live_cells & shift(pattern_floor, direction), direction)
                        & pattern_floor
                    )
                else:
                    live_cells |= (
                        shift(live_cells, direction)
                        & shift(pattern_floor, direction ^ 1)
                        & pattern_floor
                    )
            if live_cells == previous:
                break
        self.live = live_cells
        cell_index = self.cell_index
        count = 0
        remaining = live_cells
        while remaining:
            cell_index[low(remaining)] = count
            count += 1
            remaining &= remaining - 1
        size = self.size
        solvable = self.solvable = [0] * binomial[count][size]
        queue = []

        def rank(boxes):
            total, position = 0, 1
            while boxes:
                total += binomial[cell_index[low(boxes)]][position]
                position += 1
                boxes &= boxes - 1
            return total

        def add(boxes, reachable):
            index = rank(boxes)
            if solvable[index] & reachable:
                return
            reachable = reach(reachable, pattern_floor & ~boxes)
            solvable[index] |= reachable
            queue.append((boxes, low(reachable)))

        def root(boxes):
            if reverse:
                add(boxes, 1 << start_player)
                return
            empty = pattern_floor & ~boxes
            while empty:
                reachable = reach(empty & -empty, pattern_floor & ~boxes)
                add(boxes, reachable)
                empty &= ~reachable

        goal_cells = []
        remaining = self.goals
        while remaining:
            goal_cells.append(low(remaining))
            remaining &= remaining - 1

        def subsets(first, chosen, left):
            if left == 0:
                root(chosen)
                return
            for index in range(first, len(goal_cells)):
                subsets(index + 1, chosen | (1 << goal_cells[index]), left - 1)

        subsets(0, 0, size)
        head = 0
        while head < len(queue):
            boxes, player = queue[head]
            head += 1
            empty = pattern_floor & ~boxes
            reachable = reach(1 << player, empty)
            for direction in range(DIRECTIONS):
                step = STEP[direction]
                if reverse:
                    movable = boxes & shift(reachable, direction) & shift(empty, direction ^ 1)
                else:
                    movable = boxes & shift(reachable & shift(empty, direction ^ 1), direction ^ 1)
                while movable:
                    cell = low(movable)
                    movable &= movable - 1
                    next_cell = cell + step
                    add(
                        boxes ^ (1 << cell) ^ (1 << next_cell),
                        1 << (cell if reverse else next_cell + step),
                    )


def pattern_good(boxes, reachable, fixed):
    table = patterns.get(fixed)
    if table is None:
        table = patterns[fixed] = Pattern(fixed)
    size = table.size
    if size < 1:
        return True
    if (boxes & ~fixed) & ~table.live:
        return False
    cell_index = table.cell_index
    moved = cell_index[low(moved_box)] if moved_box and fixed == parent_frozen else -1
    if moved_box & fixed:
        moved = -1
    indices = []
    remaining = boxes & ~fixed
    while remaining:
        indices.append(cell_index[low(remaining)])
        remaining &= remaining - 1
    solvable = table.solvable
    count = len(indices)
    b2 = [row[2] for row in binomial]
    b3 = [row[SMALL_PATTERN_SIZE] for row in binomial]
    b4 = [row[FOUR_BOX_PATTERN_SIZE] for row in binomial]
    b5 = [row[LARGE_PATTERN_SIZE] for row in binomial]
    for first in range(count):
        a = indices[first]
        if size == 1:
            if not solvable[a] & reachable:
                return False
            continue
        for second in range(first + 1, count):
            b = indices[second]
            pair_rank = a + b2[b]
            if size == 2:
                if moved >= 0 and a != moved and b != moved:
                    continue
                if not solvable[pair_rank] & reachable:
                    return False
                continue
            for third in range(second + 1, count):
                c = indices[third]
                if size == SMALL_PATTERN_SIZE:
                    if moved >= 0 and a != moved and b != moved and c != moved:
                        continue
                    if not solvable[pair_rank + b3[c]] & reachable:
                        return False
                    continue
                for fourth in range(third + 1, count):
                    d = indices[fourth]
                    if size == FOUR_BOX_PATTERN_SIZE:
                        if moved >= 0 and moved not in (a, b, c, d):
                            continue
                        if not solvable[pair_rank + b3[c] + b4[d]] & reachable:
                            return False
                        continue
                    for fifth in range(fourth + 1, count):
                        e = indices[fifth]
                        if moved >= 0 and moved not in (a, b, c, d, e):
                            continue
                        if not solvable[pair_rank + b3[c] + b4[d] + b5[e]] & reachable:
                            return False
    return True


def pull_edges(frozen):
    """For every cell, the cells a box there comes from in one push, with the cell
    the player stands on; frozen boxes are walls."""
    edges = edge_cache.get(frozen)
    if edges is None:
        available = floor & ~frozen
        edges = [[] for _ in range(CELL_COUNT)]
        for cell in range(CELL_COUNT):
            if not available >> cell & 1:
                continue
            for direction in range(DIRECTIONS):
                next_cell = cell + STEP[direction]
                support = cell - STEP[direction] if reverse else next_cell + STEP[direction]
                if (
                    0 <= next_cell < CELL_COUNT
                    and 0 <= support < CELL_COUNT
                    and available >> next_cell & 1
                    and available >> support & 1
                ):
                    edges[cell].append((next_cell, support))
        edge_cache[frozen] = edges
    return edges


def goal_distances(frozen, boxes):
    """Pushes of a lone box from every cell to every goal; crossing another box costs
    the crossing penalty."""
    edges = pull_edges(frozen)
    table = []
    if crossing_penalty:
        penalty = [0] * CELL_COUNT
        remaining = boxes
        while remaining:
            penalty[(remaining & -remaining).bit_length() - 1] = crossing_penalty
            remaining &= remaining - 1
    for target in goals:
        distance = [UNREACHABLE] * CELL_COUNT
        distance[target] = 0
        table.append(distance)
        if frozen >> target & 1:
            continue
        if not crossing_penalty:
            queue = [target]
            head = 0
            while head < len(queue):
                cell = queue[head]
                head += 1
                current = distance[cell] + 1
                for next_cell, _ in edges[cell]:
                    if distance[next_cell] == UNREACHABLE:
                        distance[next_cell] = current
                        queue.append(next_cell)
        else:
            # a ring buffer; a cell is queued at most once at a time
            queue = [0] * DISTANCE_RING
            queued = [False] * CELL_COUNT
            queue[0] = target
            queued[target] = True
            head, tail = 0, 1
            while head != tail:
                cell = queue[head]
                head = (head + 1) & DISTANCE_RING_MASK
                queued[cell] = False
                current = distance[cell] + 1 + penalty[cell]
                for next_cell, support in edges[cell]:
                    candidate = current + penalty[support]
                    if candidate < distance[next_cell]:
                        distance[next_cell] = candidate
                        if not queued[next_cell]:
                            queue[tail] = next_cell
                            tail = (tail + 1) & DISTANCE_RING_MASK
                            queued[next_cell] = True
    return table


def by_cell(table, cells=None):
    """For every cell (or only the given ones), its distances to the goals, the goal
    j at index j + 1."""
    rows = [None] * CELL_COUNT
    for cell in range(CELL_COUNT) if cells is None else cells:
        rows[cell] = [0] + [distance[cell] for distance in table]
    return rows


def heuristic(boxes, reachable):
    if inaccessible_boxes(boxes, reachable) & ~targets:
        return -1
    frozen = frozen_boxes(boxes)
    if frozen & ~targets:
        return -1
    if use_regional and (
        not packing_good(boxes, reachable, frozen) or not region_good(boxes, reachable)
    ):
        return -1
    if pattern_size and not pattern_good(boxes, reachable, frozen):
        return -1
    cached = heuristic_cache.get(boxes)
    if cached is not None:
        return cached
    if not crossing_penalty:
        table = distance_cache.get(frozen)
        if table is None:
            table = distance_cache[frozen] = by_cell(goal_distances(frozen, boxes))
    else:
        table = by_cell(goal_distances(frozen, boxes), box_rows(boxes)[1:])
    global parent_dual
    value = -1
    if parent_dual is None and parent_boxes:
        parent_dual = expansion_dual(parent_boxes) or False
    if parent_dual and frozen == parent_dual[0]:
        value = reassign(parent_dual, moved_from, moved_to, table)
    if value < 0:
        value = assign(box_rows(boxes), table)[0]
    heuristic_cache[boxes] = value
    return value


def box_rows(boxes):
    """The cells of the boxes, as rows 1.. of the assignment (row 0 unused)."""
    rows = [0]
    while boxes:
        rows.append((boxes & -boxes).bit_length() - 1)
        boxes &= boxes - 1
    return rows


def augment(costs, box_potential, goal_potential, matched, row):
    """Add one row to an optimal partial assignment (Hungarian method); False if no
    finite augmenting path exists."""
    size = len(matched)
    previous_goal = [0] * size
    matched[0] = row
    current = 0
    slack = [UNREACHABLE] * size
    visited = [False] * size
    while True:
        visited[current] = True
        box = matched[current]
        box_costs = costs[box]
        box_value = box_potential[box]
        adjustment = UNREACHABLE
        next_goal = 0
        for j in range(1, size):
            if not visited[j]:
                reduced = box_costs[j] - box_value - goal_potential[j]
                if reduced < slack[j]:
                    slack[j] = reduced
                    previous_goal[j] = current
                if slack[j] < adjustment:
                    adjustment = slack[j]
                    next_goal = j
        if adjustment >= UNREACHABLE:
            return False
        for j in range(size):
            if visited[j]:
                box_potential[matched[j]] += adjustment
                goal_potential[j] -= adjustment
            else:
                slack[j] -= adjustment
        current = next_goal
        if not matched[current]:
            break
    while True:
        next_goal = previous_goal[current]
        matched[current] = matched[next_goal]
        current = next_goal
        if not current:
            return True


def assign(rows, table):
    """Minimum total cost of boxes to distinct goals, -1 if none is finite, with
    the potentials and the matching."""
    size = len(rows)
    costs = [table[cell] for cell in rows]
    box_potential = [0] * size
    goal_potential = [0] * size
    matched = [0] * size
    for row in range(1, size):
        if not augment(costs, box_potential, goal_potential, matched, row):
            return -1, None
    for j in range(1, size):
        if costs[matched[j]][j] >= UNREACHABLE:
            return -1, None
    return -goal_potential[0], (rows, costs, box_potential, goal_potential, matched)


def reassign(dual, old_cell, new_cell, table):
    """The assignment after one box moved: the optimal potentials of the parent stay
    feasible for the other boxes, so one augmentation suffices; -1 to recompute."""
    _, rows, costs, box_potential, goal_potential, matched = dual
    row = rows.index(old_cell)
    costs = costs[:]
    new_costs = costs[row] = table[new_cell]
    goal_potential = goal_potential[:]
    box_potential = box_potential[:]
    matched = matched[:]
    size = len(matched)
    lowest = UNREACHABLE
    for j in range(1, size):
        if matched[j] == row:
            matched[j] = 0
        reduced = new_costs[j] - goal_potential[j]
        if reduced < lowest:
            lowest = reduced
    box_potential[row] = lowest
    if not augment(costs, box_potential, goal_potential, matched, row):
        return -1
    total = 0
    for j in range(1, size):
        cost = costs[matched[j]][j]
        if cost >= UNREACHABLE:
            return -1
        total += cost
    return total


def expansion_dual(boxes):
    """The parent's optimal assignment, reused by its children's estimates."""
    if crossing_penalty:
        return None
    frozen = frozen_boxes(boxes)
    table = distance_cache.get(frozen)
    if table is None:
        return None
    value, dual = assign(box_rows(boxes), table)
    if value < 0:
        return None
    return (frozen,) + dual


def time_up():
    return perf_counter() - STARTED > FAST_SECONDS


def attempt(pull, penalty, regional, table_size, limit):
    global reverse, crossing_penalty, use_regional, pattern_size, moved_box, parent_frozen
    global goals, live, targets, parent_dual, parent_boxes, moved_from, moved_to
    parent_dual = None
    parent_boxes = 0
    reverse = pull
    crossing_penalty = penalty
    use_regional = regional
    pattern_size = table_size
    moved_box = parent_frozen = 0
    del node_state[:], node_parent[:], node_move[:]
    seen.clear()
    heuristic_cache.clear()
    distance_cache.clear()
    edge_cache.clear()
    patterns.clear()
    targets = start_boxes if reverse else goal
    goals = []
    remaining = targets
    while remaining:
        goals.append(low(remaining))
        remaining &= remaining - 1
    live = targets
    while True:
        previous = live
        for direction in range(DIRECTIONS):
            if reverse:
                live |= shift(live & shift(floor, direction), direction) & floor
            else:
                live |= shift(live, direction) & shift(floor, direction ^ 1) & floor
        if live == previous:
            break
    open_list = []
    depth = []

    def add(boxes, reachable, parent, encoded, push_depth):
        state = boxes | (low(reachable) << PLAYER_SHIFT)
        if state in seen:
            return
        estimate = heuristic(boxes, reachable)
        if estimate >= 0 and use_regional and packing_weight:
            fixed = boxes & goal
            missing = MAX_BOXES
            for remaining_goals, _ in packing_residues(fixed):
                missing = min(missing, bits(remaining_goals & ~boxes))
            estimate += packing_weight * missing
        if estimate < 0:
            if fast_mode:
                insert(state, NO_PARENT, 0)
                depth.append(-1)
            return
        node = insert(state, parent, encoded)
        depth.append(push_depth)
        score = PRIORITY_SCALE * (estimate - (push_depth if use_regional else 0))
        heapq.heappush(open_list, score * ID_SCALE - node)

    if reverse:
        todo = floor & ~goal
        while todo:
            reachable = reach(todo & -todo, floor & ~goal)
            add(goal, reachable, NO_PARENT, 0, 0)
            todo &= ~reachable
    else:
        add(start_boxes, reach(1 << start_player, floor & ~start_boxes), NO_PARENT, 0, 0)
    expanded = 0
    solved = -1
    initial_reach = reach(1 << start_player, floor & ~start_boxes)
    while open_list and expanded < limit:
        if fast_mode and (
            len(node_state) >= NODE_CAP or (expanded & CLOCK_CHECK_MASK == 0 and time_up())
        ):
            break
        node = (-heapq.heappop(open_list)) % ID_SCALE
        state = node_state[node]
        boxes = state & BOX_BITS
        reachable = reach(1 << (state >> PLAYER_SHIFT), floor & ~boxes)
        if boxes == targets and (not reverse or reachable & initial_reach):
            solved = node
            break
        expanded += 1
        if pattern_size:
            parent_frozen = frozen_boxes(boxes)
        parent_dual = None
        parent_boxes = boxes
        empty = floor & ~boxes
        allowed = restrict_corral(boxes, reachable) if not reverse else boxes
        next_depth = depth[node] + 1
        if reverse:
            movables = (
                boxes & ((reachable & (empty << BOARD_WIDTH) & live) << BOARD_WIDTH),
                boxes & ((reachable & (empty >> BOARD_WIDTH) & live) >> BOARD_WIDTH),
                boxes & ((reachable & (empty << 1) & live) << 1),
                boxes & ((reachable & (empty >> 1) & live) >> 1),
            )
        else:
            empty_live = empty & live
            movables = (
                allowed & (reachable >> BOARD_WIDTH) & (empty_live << BOARD_WIDTH),
                allowed & (reachable << BOARD_WIDTH) & (empty_live >> BOARD_WIDTH),
                allowed & (reachable >> 1) & (empty_live << 1),
                allowed & (reachable << 1) & (empty_live >> 1),
            )
        for direction in range(DIRECTIONS):
            step = STEP[direction]
            movable = movables[direction]
            while movable:
                cell = low(movable)
                movable &= movable - 1
                next_cell = cell + step
                next_boxes = boxes ^ (1 << cell) ^ (1 << next_cell)
                next_reach = reach(
                    1 << (next_cell + step if reverse else cell), floor & ~next_boxes
                )
                moved_box = 1 << next_cell
                moved_from, moved_to = cell, next_cell
                add(next_boxes, next_reach, node, cell * DIRECTIONS + direction, next_depth)
    parent_dual = None
    parent_boxes = 0
    plan = reconstruct(solved) if solved >= 0 else ""
    return plan if len(plan) <= MAX_PLAN_LENGTH else ""


def turn_letters(plan, mapping):
    out = []
    for letter in plan:
        upper = letter < "a"
        mapped = mapping[LETTERS.index(letter.lower())]
        out.append(mapped.upper() if upper else mapped)
    return "".join(out)


def transform_cell(cell, symmetry):
    if symmetry & REFLECTION_FLAG:
        cell = (cell // BOARD_WIDTH) * BOARD_WIDTH + BOARD_WIDTH - 1 - cell % BOARD_WIDTH
    for _ in range(symmetry & ROTATION_MASK):
        cell = rotate_cell(cell)
    return cell


def transform_mask(mask, symmetry):
    result = 0
    while mask:
        result |= 1 << transform_cell(low(mask), symmetry)
        mask &= mask - 1
    return result


def run_fast():
    global floor, goal, start_boxes, start_player, packing_weight
    plan = attempt(False, 1, False, 0, INITIAL_EXPANSIONS)
    if plan:
        return plan
    saved = (floor, goal, start_boxes, start_player)
    best_symmetry = 0
    best = (floor, goal, start_boxes, start_player)
    for symmetry in range(1, SYMMETRIES):
        geometry = (
            transform_mask(saved[0], symmetry),
            transform_mask(saved[1], symmetry),
            transform_mask(saved[2], symmetry),
            transform_cell(saved[PLAYER_INDEX], symmetry),
        )
        if geometry < best:
            best = geometry
            best_symmetry = symmetry
    floor, goal, start_boxes, start_player = best
    packing.clear()
    del regions[:]
    packing_weight = PACKING_WEIGHT
    plan = attempt(False, 0, True, 0, UNBOUNDED)
    probe = DIRECTION_PROBE_CELL
    inverse = [0] * DIRECTIONS
    for direction in range(DIRECTIONS):
        step = transform_cell(probe + STEP[direction], best_symmetry) - transform_cell(
            probe, best_symmetry
        )
        for j in range(DIRECTIONS):
            if STEP[j] == step:
                inverse[j] = direction
    plan = turn_letters(plan, "".join(LETTERS[inverse[d]] for d in range(DIRECTIONS)))
    floor, goal, start_boxes, start_player = saved
    return plan


def length_fallback():
    global reverse, crossing_penalty, pattern_size, moved_box
    reverse = False
    crossing_penalty = pattern_size = 0
    moved_box = 0
    del node_state[:], node_parent[:], node_move[:]
    seen.clear()
    heuristic_cache.clear()
    distance_cache.clear()
    edge_cache.clear()
    patterns.clear()
    cost = [0]
    insert(start_boxes | (start_player << PLAYER_SHIFT), NO_PARENT, 0)
    open_list = [(0, 0, 0)]
    while open_list:
        _, path_cost, node = heapq.heappop(open_list)
        if path_cost != cost[node]:
            continue
        state = node_state[node]
        boxes = state & BOX_BITS
        player = state >> PLAYER_SHIFT
        if boxes == goal:
            return reconstruct(node)
        walk = [-1] * CELL_COUNT
        walk[player] = 0
        queue = [player]
        head = 0
        reachable = 0
        free = floor & ~boxes
        while head < len(queue):
            cell = queue[head]
            head += 1
            reachable |= 1 << cell
            for direction in range(DIRECTIONS):
                next_cell = cell + STEP[direction]
                if 0 <= next_cell < CELL_COUNT and free >> next_cell & 1 and walk[next_cell] < 0:
                    walk[next_cell] = walk[cell] + 1
                    queue.append(next_cell)
        for direction in range(DIRECTIONS):
            movable = boxes & shift(reachable, direction) & shift(free & live, direction ^ 1)
            while movable:
                cell = low(movable)
                movable &= movable - 1
                next_cell = cell + STEP[direction]
                next_cost = path_cost + walk[cell - STEP[direction]] + 1
                if next_cost > MAX_PLAN_LENGTH:
                    continue
                next_boxes = boxes ^ (1 << cell) ^ (1 << next_cell)
                state = next_boxes | (cell << PLAYER_SHIFT)
                next_node = seen.get(state, -1)
                if next_node >= 0 and cost[next_node] <= next_cost:
                    continue
                estimate = heuristic(next_boxes, reach(1 << cell, floor & ~next_boxes))
                if estimate < 0 or next_cost + estimate > MAX_PLAN_LENGTH:
                    continue
                if next_node < 0:
                    next_node = insert(state, node, cell * DIRECTIONS + direction)
                    cost.append(next_cost)
                else:
                    node_parent[next_node] = node
                    node_move[next_node] = cell * DIRECTIONS + direction
                    cost[next_node] = next_cost
                heapq.heappush(open_list, (next_cost + estimate, next_cost, next_node))
    return ""


def run_safe():
    plan = ""
    if not plan:
        limit = (
            SMALL_BOX_EXPANSIONS if bits(start_boxes) <= SMALL_BOX_COUNT else MANY_BOX_EXPANSIONS
        )
        plan = attempt(False, 0, False, SMALL_PATTERN_SIZE, limit)
    if not plan:
        plan = attempt(False, 0, False, LARGE_PATTERN_SIZE, UNBOUNDED)
    if not plan:
        plan = length_fallback()
    return plan


def valid(plan, level):
    level_floor, level_goal, boxes, player = level
    if len(plan) > MAX_PLAN_LENGTH:
        return False
    for letter in plan:
        push = letter < "a"
        direction = "udlr".find(letter.lower())
        if direction < 0:
            return False
        next_cell = player + STEP[direction]
        if next_cell < 0 or next_cell >= CELL_COUNT or not level_floor >> next_cell & 1:
            return False
        if boxes >> next_cell & 1:
            destination = next_cell + STEP[direction]
            if (
                not push
                or destination < 0
                or destination >= CELL_COUNT
                or not level_floor >> destination & 1
                or boxes >> destination & 1
            ):
                return False
            boxes ^= (1 << next_cell) | (1 << destination)
        elif push:
            return False
        player = next_cell
    return boxes == level_goal


def main():
    global floor, goal, start_boxes, start_player, fast_mode
    rows = [line.rstrip("\r") for line in sys.stdin.read().split("\n")]
    rows = [line for line in rows if line]
    level_floor = level_goal = level_boxes = 0
    level_player = 0
    for row, line in enumerate(rows):
        for column, tile in enumerate(line[:BOARD_WIDTH]):
            cell = row * BOARD_WIDTH + column
            if tile != "#":
                level_floor |= 1 << cell
            if tile in ".*+":
                level_goal |= 1 << cell
            if tile in "$*":
                level_boxes |= 1 << cell
            if tile in "@+":
                level_player = cell
    level_floor = reach(1 << level_player, level_floor)
    level_goal &= level_floor
    level_boxes &= level_floor
    level = (level_floor, level_goal, level_boxes, level_player)
    if level_boxes == level_goal:
        sys.stdout.write("\n")
        return
    floor, goal, start_boxes, start_player = level
    try:
        plan = run_fast()
    except FailedWalk:
        plan = ""
    if not valid(plan, level):
        packing.clear()
        del regions[:]
        fast_mode = False
        floor, goal, start_boxes, start_player = level
        plan = run_safe()
    sys.stdout.write(plan + "\n")


main()
