import sys

# bridgeless cubic maps with the whole border built, found by a search
BLOCKS = [
    [r"O-O-O-O", r"|\|/ /|", r"O O O-O", r"|\   \|", r"O-O O O", r"|/ /|\|", r"O-O-O-O"],
    [
        r"O-O-O-O",
        r"|\ \|/|",
        r"O-O O O",
        r"| |  /|",
        r"O-O-O-O",
        r"|     |",
        r"O-O O-O",
        r"|/| |\|",
        r"O-O-O-O",
    ],
    [
        r"O-O-O-O",
        r"|\|/ /|",
        r"O O O-O",
        r"|\   \|",
        r"O-O-O O",
        r"|   |\|",
        r"O-O O O",
        r"|/|/ \|",
        r"O O O O",
        r"|/ /|\|",
        r"O-O-O-O",
    ],
    [
        r"O-O-O-O",
        r"|\ \|/|",
        r"O O O O",
        r"|\|\ /|",
        r"O O O-O",
        r"|\|   |",
        r"O-O O-O",
        r"|   |\|",
        r"O-O-O O",
        r"| |  \|",
        r"O-O O O",
        r"|/ /|\|",
        r"O-O-O-O",
    ],
    [
        r"O-O-O-O-O-O",
        r"|\ \|  \|/|",
        r"O-O O-O O O",
        r"| |  /|  /|",
        r"O-O O O O-O",
        r"|/ /| |\ \|",
        r"O-O-O-O-O-O",
    ],
    [
        r"O-O-O-O-O-O",
        r"|\ \ \ \|/|",
        r"O-O-O O O O",
        r"|    \|\ /|",
        r"O-O-O-O O O",
        r"| | |  / /|",
        r"O-O O O O-O",
        r"|/ /| |\ \|",
        r"O-O-O-O-O-O",
    ],
    [
        r"O-O-O-O-O-O",
        r"|\|  \| |/|",
        r"O-O O O-O O",
        r"|  /|\   /|",
        r"O-O-O O O-O",
        r"|  / /|/  |",
        r"O O-O O O-O",
        r"|\ \ \|/ \|",
        r"O-O O O O O",
        r"|/ /|  /|\|",
        r"O-O-O-O-O-O",
    ],
    [
        r"O-O-O-O-O-O",
        r"|\| |  \|/|",
        r"O-O O O O O",
        r"|  /|/|\ /|",
        r"O-O-O O-O O",
        r"|     |  /|",
        r"O-O-O O O-O",
        r"| | |\|\| |",
        r"O-O O O O-O",
        r"|  \|\ \  |",
        r"O-O O O O-O",
        r"|/| | |\ \|",
        r"O-O-O-O-O-O",
    ],
    [
        r"O-O-O-O-O-O-O-O",
        r"|\ \ \| | |/ /|",
        r"O-O O O O O O-O",
        r"|/ /| | |\ \ \|",
        r"O-O-O-O-O-O-O-O",
    ],
    [
        r"O-O-O-O-O-O-O-O-O-O",
        r"|\ \ \|  \| |/ / /|",
        r"O-O O O O-O O O O-O",
        r"|/ /| | |\  | |\ \|",
        r"O-O-O-O-O-O-O-O-O-O",
    ],
    [
        r"O-O-O-O-O-O-O-O-O-O-O-O",
        r"|\ \ \ \|/ /  | | |/ /|",
        r"O-O O O O O-O O-O O O-O",
        r"|/ /| |\  | |\ \ \ \ \|",
        r"O-O-O-O-O-O-O-O-O-O-O-O",
    ],
    [
        r"O-O-O-O-O-O-O-O-O-O-O-O-O-O",
        r"|\ \| |/   \ \|/ /  |/ / /|",
        r"O-O O O O-O-O O O O-O O O-O",
        r"|/ / / /| | |  /| |\  |\ \|",
        r"O-O-O-O-O-O-O-O-O-O-O-O-O-O",
    ],
]
MIN_SIDE = 3
FLAT = 3  # a strip this high needs at least FLAT_STEP columns
FLAT_STEP = 8
FLAT_TOP = 14
STEP = 4
WIDE_TOP = 6
TALL_TOP = 7
NO_WORLD = "Imaginary world"


def split(n, step, top):
    parts = []
    while n > top:
        parts.append(step)
        n -= step
    return parts + [n]


def main():
    w, h = map(int, sys.stdin.read().split())
    if w * h % 2 == 1 or min(w, h) < MIN_SIDE:
        print(NO_WORLD)
        return
    turned = w % 2 == 1  # then h is even: build the turned map
    if turned:
        w, h = h, w
    if h == FLAT:
        if w < FLAT_STEP:
            print(NO_WORLD)
            return
        widths, heights = split(w, FLAT_STEP, FLAT_TOP), [FLAT]
    else:
        widths, heights = split(w, STEP, WIDE_TOP), split(h, STEP, TALL_TOP)
    shapes = {(len(b[0]) // 2 + 1, len(b) // 2 + 1): b for b in BLOCKS}
    grid = [[" "] * (2 * w - 1) for _ in range(2 * h - 1)]
    top = 0
    for j, bh in enumerate(heights):
        left = 0
        for i, bw in enumerate(widths):
            y, x = 2 * top, 2 * left
            for r, row in enumerate(shapes[bw, bh]):
                grid[y + r][x : x + len(row)] = row
            if i > 0:
                # two vertical bridges at the seam, in the lowest two rows,
                # give way to two horizontal ones
                z = 2 * (top + bh - 2)
                grid[z + 1][x - 2] = grid[z + 1][x] = " "
                grid[z][x - 1] = grid[z + 2][x - 1] = "-"
            left += bw
        if j > 0:
            # the same exchange across a horizontal seam, in the last two columns
            y, x = 2 * top, 2 * (w - 2)
            grid[y - 2][x + 1] = grid[y][x + 1] = " "
            grid[y - 1][x] = grid[y - 1][x + 2] = "|"
        top += bh
    if turned:
        swap = {"-": "|", "|": "-"}
        grid = [[swap.get(row[c], row[c]) for row in grid] for c in range(len(grid[0]))]
    print("\n".join("".join(row) for row in grid))


main()
