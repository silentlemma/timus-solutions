import sys

# the places a stick can take in one cell of the picture
TOP = 1
MIDDLE = TOP << 1
BOTTOM = MIDDLE << 1
UPPER_LEFT = BOTTOM << 1
UPPER_RIGHT = UPPER_LEFT << 1
LOWER_LEFT = UPPER_RIGHT << 1
LOWER_RIGHT = LOWER_LEFT << 1
UPPER_SLASH = LOWER_RIGHT << 1
LOWER_SLASH = UPPER_SLASH << 1
PLUS_UPRIGHT = LOWER_SLASH << 1
EQUAL_UPPER = PLUS_UPRIGHT << 1
EQUAL_LOWER = EQUAL_UPPER << 1
SIDES = UPPER_LEFT | UPPER_RIGHT | LOWER_LEFT | LOWER_RIGHT
SHAPES = {
    "0": TOP | SIDES | BOTTOM,
    "1": UPPER_SLASH | UPPER_RIGHT | LOWER_RIGHT,
    "2": TOP | UPPER_RIGHT | LOWER_SLASH | BOTTOM,
    "3": TOP | UPPER_SLASH | MIDDLE | LOWER_SLASH,
    "4": UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_RIGHT,
    "5": TOP | UPPER_LEFT | MIDDLE | LOWER_RIGHT | BOTTOM,
    "6": UPPER_SLASH | MIDDLE | LOWER_LEFT | LOWER_RIGHT | BOTTOM,
    "7": TOP | UPPER_SLASH | LOWER_LEFT,
    "8": TOP | SIDES | MIDDLE | BOTTOM,
    "9": TOP | UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_SLASH,
    "+": MIDDLE | PLUS_UPRIGHT,  # the bar of the plus lies where a middle stick does
    "=": EQUAL_UPPER | EQUAL_LOWER,
}
LONGEST = 8  # digits in a number
BASE = 10


def sticks(shape):
    return bin(shape).count("1")


def solve(text, k):
    cells = [SHAPES[c] for c in text]
    n = len(cells)
    total = sum(map(sticks, cells))

    def kept(pos, ch):
        """Sticks of cell pos that stay in place if it shows ch."""
        return sticks(cells[pos] & SHAPES[ch])

    digits = n - 2
    for len_x in range(1, LONGEST + 1):
        for len_y in range(1, LONGEST + 1):
            len_z = digits - len_x - len_y
            # no leading zeros, so z has at least as many digits as x and y
            if not max(len_x, len_y) <= len_z <= LONGEST:
                continue
            plus, equal = len_x, len_x + len_y + 1
            # states after some columns, from the right: (carry, sticks used)
            # -> (sticks kept in place, the column's digits, previous state)
            layer = {
                (0, sticks(SHAPES["+"]) + sticks(SHAPES["="])): (
                    kept(plus, "+") + kept(equal, "="),
                    None,
                )
            }
            history = []
            for col in range(len_z):
                pos_x = len_x - 1 - col if col < len_x else None
                pos_y = len_x + len_y - col if col < len_y else None
                pos_z = n - 1 - col
                # the moves of one column, the best kept count for each
                # carry in, carry out and number of sticks
                moves = {}
                for carry in range(2):
                    for dx in range(BASE) if pos_x is not None else (0,):
                        if pos_x is not None and dx == 0 and col == len_x - 1 and len_x > 1:
                            continue
                        for dy in range(BASE) if pos_y is not None else (0,):
                            if pos_y is not None and dy == 0 and col == len_y - 1 and len_y > 1:
                                continue
                            dz, out = (dx + dy + carry) % BASE, (dx + dy + carry) // BASE
                            if dz == 0 and col == len_z - 1 and len_z > 1:
                                continue
                            cx, cy, cz = str(dx), str(dy), str(dz)
                            used = sticks(SHAPES[cz])
                            gain = kept(pos_z, cz)
                            if pos_x is not None:
                                used += sticks(SHAPES[cx])
                                gain += kept(pos_x, cx)
                            if pos_y is not None:
                                used += sticks(SHAPES[cy])
                                gain += kept(pos_y, cy)
                            key = (carry, out, used)
                            if key not in moves or moves[key][0] < gain:
                                moves[key] = (gain, cx, cy, cz)
                nxt = {}
                for (carry, used), (have, _) in layer.items():
                    for (c_in, out, more), (gain, cx, cy, cz) in moves.items():
                        if c_in != carry or used + more > total:
                            continue
                        state = (out, used + more)
                        if state not in nxt or nxt[state][0] < have + gain:
                            nxt[state] = (have + gain, (cx, cy, cz, carry, used))
                history.append(nxt)
                layer = nxt
            # every stick must be used, and the moved ones are those not kept
            final = layer.get((0, total))
            if final is None or total - final[0] > k:
                continue
            xs, ys, zs = [], [], []
            state = (0, total)
            for col in range(len_z - 1, -1, -1):
                cx, cy, cz, carry, used = history[col][state][1]
                if col < len_x:
                    xs.append(cx)
                if col < len_y:
                    ys.append(cy)
                zs.append(cz)
                state = (carry, used)
            return "".join(xs) + "+" + "".join(ys) + "=" + "".join(zs)
    return "Impossible"


def main():
    tokens = sys.stdin.read().split()
    print(solve("".join(tokens[:-1]), int(tokens[-1])))


main()
