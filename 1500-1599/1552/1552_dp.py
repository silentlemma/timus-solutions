from array import array

CELLS = 4  # the program needs at most four cells
VALUES = 27  # a cell holds 0 or a letter, kept as 0 or 1 to 26
OTHERS = VALUES ** (CELLS - 1)  # states of the cells away from the pointer
STATES = CELLS * OTHERS
LETTER_BASE = ord("a") - 1
NONE = -1
UNREACHABLE = 1 << 30


def main():
    s = input().strip()
    target = [ord(c) - LETTER_BASE for c in s]
    # a state, after a letter is printed, is the pointer's cell (holding that
    # letter) and the values of the other three cells, left to right; the
    # used cells form a block of four that holds the start cell somewhere
    cost = array("i", [UNREACHABLE]) * STATES
    for start in range(CELLS):
        cost[start * OTHERS] = 0
    came_from = []
    previous = 0  # the value under the pointer: 0 before the first letter
    for letter in target:
        nxt = array("i", [UNREACHABLE]) * STATES
        back = array("i", [NONE]) * STATES
        for state in range(STATES):
            here = cost[state]
            if here == UNREACHABLE:
                continue
            p, rest = divmod(state, OTHERS)
            # the four values, the pointer's cell holding the last letter
            w = [0] * CELLS
            digits = [rest // (VALUES * VALUES), rest // VALUES % VALUES, rest % VALUES]
            k = 0
            for cell in range(CELLS):
                if cell == p:
                    w[cell] = previous
                else:
                    w[cell] = digits[k]
                    k += 1
            for q in range(CELLS):
                old = w[q]
                change = letter - old if old else letter + LETTER_BASE
                total = here + abs(p - q) + abs(change) + 1
                code = 0
                for cell in range(CELLS):
                    if cell != q:
                        code = code * VALUES + w[cell]
                code += q * OTHERS
                if total < nxt[code]:
                    nxt[code] = total
                    back[code] = state
        came_from.append(back)
        cost = nxt
        previous = letter
    # walk back to recover the cells used, then write the program
    state = min(range(STATES), key=lambda st: cost[st])
    cells = []
    for back in reversed(came_from):
        cells.append(state // OTHERS)
        state = back[state]
    cells.append(state // OTHERS)  # the start
    cells.reverse()
    values = [0] * CELLS
    out = []
    for i, letter in enumerate(target):
        p, q = cells[i], cells[i + 1]
        out.append(">" * (q - p) if q > p else "<" * (p - q))
        old = values[q]
        change = letter - old if old else letter + LETTER_BASE
        out.append("+" * change if change > 0 else "-" * -change)
        out.append(".")
        values[q] = letter
    print("".join(out))


main()
