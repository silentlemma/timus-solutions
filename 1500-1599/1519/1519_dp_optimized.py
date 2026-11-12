import sys

OPEN, CLOSE = 1, 2
FLIP = OPEN ^ CLOSE
BITS = 2
MASK = 3
FREE = ord(".")
MIN_SPLIT_WIDTH = 8
MIDDLE_DIVISOR = 3
SHORT_JOIN = 6


def group_profiles(ways):
    groups = {}
    for state, count in ways.items():
        if state == 0:
            continue
        active = 0
        column = 0
        stack = []
        partners = []
        edges = 0
        while state:
            plug = state & MASK
            if plug:
                active |= 1 << column
                index = len(partners)
                if plug == OPEN:
                    stack.append(index)
                    partners.append(-1)
                else:
                    opening = stack.pop()
                    partners[opening] = index
                    partners.append(opening)
                    edges |= 1 << (index * (index - 1) // 2 + opening)
            state >>= BITS
            column += 1
        groups.setdefault(active, []).append((partners, edges, count))
    return groups


def join_mirrored_halves(ways, width, reflect_columns):
    total = 0
    for active, group in group_profiles(ways).items():
        multiplier = 1
        if reflect_columns:
            mirror = 0
            for column in range(width):
                mirror = (mirror << 1) | (active >> column & 1)
            if active > mirror:
                continue
            if active < mirror:
                multiplier = 2
        size = len(group[0][0])
        if size == 2:
            # With two endpoints there is exactly one possible pairing.
            total += multiplier * group[0][2] ** 2
            continue
        for i, (first, first_edges, first_count) in enumerate(group):
            for j in range(i):
                second, second_edges, second_count = group[j]
                # An edge used by both halves is already a separate loop.
                if first_edges & second_edges:
                    continue
                # Disjoint pairings can only have cycles of length four or more.
                if size <= SHORT_JOIN:
                    total += multiplier * 2 * first_count * second_count
                    continue
                end = second[first[0]]
                visited = 2
                while end != 0:
                    end = second[first[end]]
                    visited += 2
                if visited == size:
                    # Swapping the two distinct pairings also gives one loop.
                    total += multiplier * 2 * first_count * second_count
    return total


def join_halves(upper, lower):
    bottom_groups = group_profiles(lower)
    total = 0
    for active, top_group in group_profiles(upper).items():
        bottom_group = bottom_groups.get(active)
        if not bottom_group:
            continue
        size = len(top_group[0][0])
        if size == 2:
            total += top_group[0][2] * bottom_group[0][2]
            continue
        for first, first_edges, first_count in top_group:
            for second, second_edges, second_count in bottom_group:
                if first_edges & second_edges:
                    continue
                if size <= SHORT_JOIN:
                    total += first_count * second_count
                    continue
                end = second[first[0]]
                visited = 2
                while end != 0:
                    end = second[first[end]]
                    visited += 2
                if visited == size:
                    total += first_count * second_count
    return total


def count_tracks(grid):
    # Crop all-obstacle borders so every interior cut separates free cells.
    occupied_rows = [row for row, line in enumerate(grid) if FREE in line]
    columns = [col for col in range(len(grid[0])) if any(row[col] == FREE for row in grid)]
    top, bottom = occupied_rows[0], occupied_rows[-1]
    left, right = columns[0], columns[-1]
    grid = [row[left : right + 1] for row in grid[top : bottom + 1]]
    if len(grid[0]) > len(grid):
        grid = list(zip(*grid))
    n, m = len(grid), len(grid[0])
    free = [[cell == FREE for cell in row] + [False] for row in grid]
    free.append([False] * (m + 1))
    cells = {(r, c) for r in range(n) for c in range(m) if free[r][c]}
    black = sum((r + c) % 2 == 0 for r, c in cells)
    if 2 * black != len(cells):
        return 0
    for r, c in cells:
        degree = sum(
            (rr, cc) in cells for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
        )
        if degree < 2:
            return 0
    pending = [next(iter(cells))]
    seen = set(pending)
    for r, c in pending:
        for other in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if other in cells and other not in seen:
                seen.add(other)
                pending.append(other)
    if len(seen) != len(cells):
        return 0
    middle = n // 2
    if n % 2 == 0 and grid == grid[::-1]:
        return join_mirrored_halves(scan(free, m, middle), m, all(row == row[::-1] for row in grid))
    if m >= MIN_SPLIT_WIDTH:
        # A narrow cut reduces the number of endpoint sets and pairings.
        margin = n // MIDDLE_DIVISOR
        crossing, _, cut = min(
            (sum(a and b for a, b in zip(free[k - 1], free[k], strict=True)), abs(k - middle), k)
            for k in range(margin, n - margin + 1)
        )
        if crossing < 2:
            return 0
        upper = scan(free, m, cut)
        lower = scan(free[-2::-1] + [free[-1]], m, n - cut)
        return join_halves(upper, lower)
    last = max(r * m + c for r, c in cells)
    return scan(free, m, n, last)


def scan(free, m, row_limit, last=-1):
    ways, spare = {0: 1}, {}
    total = 0
    for i in range(row_limit):
        for j in range(m):
            spare.clear()
            get = spare.get
            sl, su = BITS * j, BITS * (j + 1)
            clear = ~(MASK << sl | MASK << su)
            down, right = free[i + 1][j], free[i][j + 1]
            if not free[i][j]:
                plug_mask = MASK << sl | MASK << su
                for state, count in ways.items():
                    if not state & plug_mask:
                        spare[state] = count
            else:
                for state, count in ways.items():
                    left, up = state >> sl & MASK, state >> su & MASK
                    base = state & clear
                    if left == 0 and up == 0:
                        if down and right:
                            out = base | OPEN << sl | CLOSE << su
                            spare[out] = get(out, 0) + count
                    elif left == 0 or up == 0:
                        end = left | up
                        if down:
                            out = base | end << sl
                            spare[out] = get(out, 0) + count
                        if right:
                            out = base | end << su
                            spare[out] = get(out, 0) + count
                    elif left == up:
                        depth = 1
                        if left == OPEN:
                            far = j + 2
                            tail = state >> (BITS * far)
                            while True:
                                plug = tail & MASK
                                if plug == OPEN:
                                    depth += 1
                                elif plug == CLOSE:
                                    depth -= 1
                                if depth == 0:
                                    break
                                tail >>= BITS
                                far += 1
                        else:
                            far = j - 1
                            while True:
                                plug = state >> (BITS * far) & MASK
                                if plug == CLOSE:
                                    depth += 1
                                elif plug == OPEN:
                                    depth -= 1
                                if depth == 0:
                                    break
                                far -= 1
                        out = base ^ FLIP << (BITS * far)
                        spare[out] = get(out, 0) + count
                    elif left == CLOSE:
                        spare[base] = get(base, 0) + count
                    elif i * m + j == last and base == 0:
                        total += count
            ways, spare = spare, ways
        if last < 0 and i + 1 == row_limit:
            return ways
        spare.clear()
        for state, count in ways.items():
            spare[state << BITS] = count
        ways, spare = spare, ways
    return total


def main():
    words = sys.stdin.buffer.read().split()
    rows = int(words[0])
    print(count_tracks(words[2 : 2 + rows]))


if __name__ == "__main__":
    main()
