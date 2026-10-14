CORNERS = 4  # a loop turns at least four times, by 90 degrees each
FIRST_STAIR = 12  # all-turn loops have 4 or at least 12 turns
NOTCHED_HEIGHT = 3  # rows of the box when a corner is cut in


def best(s, t):
    """Most straights and turns usable: both even, at least 4 turns, and
    without straights the turns must be 4 or a multiple of 4 from 12."""
    straights, turns = s - s % 2, t - t % 2
    if turns < CORNERS:
        return None
    if straights == 0:
        turns = turns - turns % CORNERS
        if turns < FIRST_STAIR:
            turns = CORNERS
    return straights, turns


def letters(cells):
    """F, L or R for every cell of a closed loop of cells."""
    out = []
    for i in range(len(cells)):
        (ax, ay), (bx, by), (cx, cy) = cells[i - 1], cells[i], cells[(i + 1) % len(cells)]
        d1, d2 = (bx - ax, by - ay), (cx - bx, cy - by)
        out.append("F" if d1 == d2 else ("L" if d1[0] * d2[1] - d1[1] * d2[0] > 0 else "R"))
    return "".join(out)


def ring(width, height, bumps, notch):
    """The cells of the border of a width x height box, counterclockwise from
    the lower left corner, with bumps (2 cells wide, 1 high) on the top and
    bottom rows, and with the lower left corner cut in if notch is set."""
    free_top = list(range(width - 2, 1, -2))  # pairs (x, x - 1) on the top row
    free_bottom = list(range(2 + notch, width - 1, 2))  # pairs (x - 1, x)
    up = min(bumps, len(free_top))
    down = bumps - up
    up_at, down_at = set(free_top[:up]), set(free_bottom[:down])
    cells = []
    if notch:
        cells += [(1, 1), (1, 0)]
    else:
        cells.append((0, 0))
    x = cells[-1][0] + 1
    while x < width:  # the bottom row, going east
        if x in down_at:
            cells += [(x - 1, -1), (x, -1), (x, 0)]
        else:
            cells.append((x, 0))
        x += 1
    cells += [(width - 1, y) for y in range(1, height)]
    x = width - 2
    while x >= 0:  # the top row, going west
        if x in up_at:
            cells += [(x, height - 1), (x, height), (x - 1, height), (x - 1, height - 1)]
            x -= 2
            continue
        cells.append((x, height - 1))
        x -= 1
    # the left column, going south; with a notch its last cell (0, 1) leads
    # into (1, 1) instead of the corner
    cells += [(0, y) for y in range(height - 2, 0, -1)]
    return cells


def build(straights, turns):
    if straights == 0 and turns >= FIRST_STAIR:
        # a staircase loop: four corners and steps LR on the sides
        steps = (turns - CORNERS) // CORNERS
        side_a, side_b = "LR" * (steps - 1), "LR"
        return ("L" + side_a + "L" + side_b) * 2
    notch = turns % CORNERS == 2
    bumps = (turns - CORNERS) // CORNERS  # a notch takes the other 2 turns
    width = 2 + straights // 2 + bumps
    cells = ring(width, NOTCHED_HEIGHT if notch else 2, bumps, notch)
    return letters(cells)


def main():
    s, t = map(int, input().split())
    found = best(s, t)
    if found is None:
        print("Atawazu")
        return
    path = build(*found)
    print(len(path))
    print(path)


main()
