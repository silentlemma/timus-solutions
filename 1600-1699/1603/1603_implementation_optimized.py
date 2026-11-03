import sys
from array import array

SIDE = 4
CELLS = SIDE * SIDE
LETTERS = 26
FIRST_LETTER = ord("a")
MASK_COUNT = 1 << CELLS

data = sys.stdin.buffer.read().split()
grid = b"".join(data[:SIDE])
positions = [0] * LETTERS
colors = [0, 0]
near = [0] * CELLS
for cell, letter in enumerate(grid):
    row, column = divmod(cell, SIDE)
    bit = 1 << cell
    positions[letter - FIRST_LETTER] |= bit
    colors[(row + column) & 1] |= bit
    for other in range(CELLS):
        other_row, other_column = divmod(other, SIDE)
        if abs(row - other_row) + abs(column - other_column) == 1:
            near[cell] |= 1 << other
capacity = [[(mask & color).bit_count() for mask in positions] for color in colors]
# One shared endpoint-bit table; recursive closures never retain old large tables.
failed = array("H", [0]) * MASK_COUNT


def found(word):
    if (
        positions[word[0] - FIRST_LETTER].bit_count()
        > positions[word[-1] - FIRST_LETTER].bit_count()
    ):
        word = word[::-1]
    length = len(word)
    needed = [[0] * LETTERS for _ in colors]
    for index, letter in enumerate(word):
        needed[index & 1][letter - FIRST_LETTER] += 1
    starts = 0
    for color in range(len(colors)):
        if all(
            needed[0][letter] <= capacity[color][letter]
            and needed[1][letter] <= capacity[color ^ 1][letter]
            for letter in range(LETTERS)
        ):
            starts |= colors[color]
    if not starts:
        return False
    # Suffix feasibility allows reuse: it is only a necessary, safe pruning test.
    allowed = [0] * length
    allowed[-1] = positions[word[-1] - FIRST_LETTER]
    for index in range(length - 2, -1, -1):
        cells = positions[word[index] - FIRST_LETTER]
        while cells:
            bit = cells & -cells
            cell = bit.bit_length() - 1
            if near[cell] & allowed[index + 1]:
                allowed[index] |= bit
            cells -= bit
    starts &= allowed[0]
    if not starts:
        return False
    failed[:] = array("H", [0]) * MASK_COUNT

    def walk(cell, used, index):
        if index + 1 == length:
            return True
        endpoint = 1 << cell
        if failed[used] & endpoint:
            return False
        options = near[cell] & allowed[index + 1] & ~used
        while options:
            bit = options & -options
            if walk(bit.bit_length() - 1, used | bit, index + 1):
                return True
            options -= bit
        failed[used] |= endpoint
        return False

    while starts:
        bit = starts & -starts
        if walk(bit.bit_length() - 1, bit, 0):
            return True
        starts -= bit
    return False


answers = {}
out = []
for word in data[SIDE + 1 : SIDE + 1 + int(data[SIDE])]:
    result = answers.get(word)
    if result is None:
        result = found(word)
        answers[word] = result
    out.append(word.decode() + (": YES" if result else ": NO"))
print("\n".join(out))
