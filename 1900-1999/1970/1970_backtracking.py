import sys


PIECE_SIZE = 4
GRID_SIDE = 3
PIECE_COUNT = GRID_SIDE * GRID_SIDE
TURN_COUNT = 4
STRIDE = PIECE_SIZE - 1
BOARD_SIDE = GRID_SIDE * STRIDE + 1
DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def rotate(piece):
    return tuple(tuple(row) for row in zip(*piece[::-1]))


def assemble(pieces):
    states = []
    masks = []
    initial = 0
    for index, piece in enumerate(pieces):
        current = tuple(tuple(row) for row in piece)
        seen = set()
        mask = 0
        for turn in range(TURN_COUNT):
            state = len(states)
            states.append(current)
            mask |= 1 << state
            if current not in seen and (index != 0 or turn == 0):
                initial |= 1 << state
            seen.add(current)
            current = rotate(current)
        masks.append(mask)
    edges = []
    for piece in states:
        edges.append((piece[0], tuple(row[-1] for row in piece),
                      piece[-1], tuple(row[0] for row in piece)))
    compatible = [[0] * len(states) for _ in DIRECTIONS]
    for direction in range(TURN_COUNT):
        opposite = (direction + 2) % TURN_COUNT
        for first, first_edges in enumerate(edges):
            for second, second_edges in enumerate(edges):
                if first // TURN_COUNT != second // TURN_COUNT:
                    if first_edges[direction] == second_edges[opposite]:
                        compatible[direction][first] |= 1 << second
    neighbors = []
    for slot in range(PIECE_COUNT):
        row, column = divmod(slot, GRID_SIDE)
        adjacent = []
        for direction, (dr, dc) in enumerate(DIRECTIONS):
            nr, nc = row + dr, column + dc
            if 0 <= nr < GRID_SIDE and 0 <= nc < GRID_SIDE:
                adjacent.append((direction, nr * GRID_SIDE + nc))
        neighbors.append(adjacent)
    placement = [-1] * PIECE_COUNT

    def search(domains, remaining):
        if remaining == 0:
            return True
        slot = min((i for i in range(PIECE_COUNT) if placement[i] < 0),
                   key=lambda i: (domains[i].bit_count(), -len(neighbors[i])))
        choices = domains[slot]
        while choices:
            bit = choices & -choices
            choices ^= bit
            state = bit.bit_length() - 1
            placement[slot] = state
            unused = ~masks[state // TURN_COUNT]
            following = [domain & unused for domain in domains]
            for direction, adjacent in neighbors[slot]:
                if placement[adjacent] < 0:
                    following[adjacent] &= compatible[direction][state]
            if all(following[i] for i in range(PIECE_COUNT) if placement[i] < 0):
                if search(following, remaining - 1):
                    return True
            placement[slot] = -1
        return False

    if not search([initial] * PIECE_COUNT, PIECE_COUNT):
        raise ValueError('The guaranteed arrangement was not found')
    board = [[0] * BOARD_SIDE for _ in range(BOARD_SIDE)]
    for slot, state in enumerate(placement):
        row, column = divmod(slot, GRID_SIDE)
        for dr in range(PIECE_SIZE):
            for dc in range(PIECE_SIZE):
                board[row * STRIDE + dr][column * STRIDE + dc] = states[state][dr][dc]
    return board


def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    pixels = PIECE_SIZE * PIECE_SIZE
    pieces = [[[numbers[index * pixels + row * PIECE_SIZE + column]
                for column in range(PIECE_SIZE)] for row in range(PIECE_SIZE)]
              for index in range(PIECE_COUNT)]
    for row in assemble(pieces):
        print(*row)


if __name__ == '__main__':
    main()
