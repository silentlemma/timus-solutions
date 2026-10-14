import sys

SIDE = 7
ARM = 2  # the corners cut from the 7 x 7 square are 2 x 2
LETTERS = "ABCDEFG"
JUMPS = ((0, 1), (1, 0), (0, -1), (-1, 0))
CLASSES = 3  # the residues behind the invariant


def on_board(r, c):
    return 0 <= r < SIDE and 0 <= c < SIDE and (ARM <= r < SIDE - ARM or ARM <= c < SIDE - ARM)


def main():
    target = sys.stdin.read().split()[0]
    tc, tr = LETTERS.index(target[0]), int(target[1]) - 1
    centre = SIDE // 2
    # A jump changes the parity of the peg count in each class of r + c
    # (mod 3), and of r - c: so the last peg sits where r and c are both
    # congruent to the centre modulo 3.
    if (tr - centre) % CLASSES or (tc - centre) % CLASSES or not on_board(tr, tc):
        print("Impossible")
        return
    # The start is symmetric, so an edge target is a quarter turn of the top
    # one: search for the top cell, which the search finds fast, then turn.
    turns = 0
    while (tr, tc) != (centre, centre) and (tr, tc) != (SIDE - 1, centre):
        tr, tc = SIDE - 1 - tc, tr  # a quarter turn back
        turns += 1
    cells = [(r, c) for r in range(SIDE) for c in range(SIDE) if on_board(r, c)]
    index = {cell: i for i, cell in enumerate(cells)}
    # every move as (from, over, to) bits
    moves = []
    for (r, c), i in index.items():
        for dr, dc in JUMPS:
            over, to = (r + dr, c + dc), (r + 2 * dr, c + 2 * dc)
            if over in index and to in index:
                moves.append((1 << i, 1 << index[over], 1 << index[to], i, index[to]))
    full = (1 << len(cells)) - 1
    start = full & ~(1 << index[(centre, centre)])
    goal = 1 << index[(tr, tc)]
    dead = set()
    path = []

    def solve(board):
        if board == goal:
            return True
        if board in dead:
            return False
        for frm, over, to, i, j in moves:
            if board & frm and board & over and not board & to:
                path.append((i, j))
                if solve(board ^ frm ^ over ^ to):
                    return True
                path.pop()
        dead.add(board)
        return False

    solve(start)

    def name(i):
        r, c = cells[i]
        for _ in range(turns):
            r, c = c, SIDE - 1 - r  # a quarter turn forward
        return "%s%d" % (LETTERS[c], r + 1)

    print("\n".join("%s-%s" % (name(i), name(j)) for i, j in path))


main()
