from array import array
from collections import deque
import sys

THIN_WALL = ord(".")


def minimum_passages(rows, columns, scheme):
    height, width = rows + 2, columns + 2
    size = height * width
    outside = bytearray(size)
    masks = bytearray(size)
    moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
    offsets = (-width, 1, width, -1)
    for position in range(size):
        row, column = divmod(position, width)
        outside[position] = (
            row == 0 or row == height - 1 or column == 0 or column == width - 1
        )
    starts = []
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            position = row * width + column
            drawing_row, drawing_column = 2 * row - 1, 2 * column - 1
            if scheme[drawing_row][drawing_column] in b"12":
                starts.append(position)
            walls = (
                scheme[drawing_row - 1][drawing_column],
                scheme[drawing_row][drawing_column + 1],
                scheme[drawing_row + 1][drawing_column],
                scheme[drawing_row][drawing_column - 1],
            )
            for direction, wall in enumerate(walls):
                if wall == THIN_WALL:
                    masks[position] |= 1 << direction
    for position in range(size):
        if not outside[position]:
            continue
        row, column = divmod(position, width)
        for direction, (dr, dc) in enumerate(moves):
            nr, nc = row + dr, column + dc
            if not (0 <= nr < height and 0 <= nc < width):
                continue
            neighbor = nr * width + nc
            opposite = (direction + 2) % len(moves)
            if outside[neighbor] or masks[neighbor] & (1 << opposite):
                masks[position] |= 1 << direction
    relative = ((0, 1), (1, -1), (1, 0), (1, 1))
    variants = len(relative)
    relative_index = {delta: index for index, delta in enumerate(relative)}
    deltas = tuple(dr * width + dc for dr, dc in relative)
    transitions = []
    for orientation, delta in enumerate(relative):
        choices = []
        for player in range(2):
            for direction, (dr, dc) in enumerate(moves):
                positions = [(0, 0), delta]
                r, c = positions[player]
                positions[player] = r + dr, c + dc
                first, second = sorted(positions)
                difference = second[0] - first[0], second[1] - first[1]
                if difference not in relative_index:
                    continue
                shift = first[0] * width + first[1]
                state_change = (
                    shift * variants + relative_index[difference] - orientation
                )
                choices.append(
                    (player, 1 << direction, state_change, offsets[direction])
                )
        transitions.append(choices)
    first, second = sorted(starts)
    initial = first * variants + deltas.index(second - first)
    distance = array("i", [-1]) * (size * variants)
    finished = bytearray(len(distance))
    distance[initial] = 0
    pending = deque([initial])
    while pending:
        state = pending.popleft()
        if finished[state]:
            continue
        finished[state] = 1
        current = distance[state]
        first, orientation = divmod(state, variants)
        second = first + deltas[orientation]
        if outside[first] and outside[second]:
            return current
        for player, mask, change, offset in transitions[orientation]:
            position = first if player == 0 else second
            if not masks[position] & mask:
                continue
            neighbor = position + offset
            cost = 0 if outside[position] and outside[neighbor] else 1
            following = state + change
            candidate = current + cost
            if distance[following] == -1 or candidate < distance[following]:
                distance[following] = candidate
                if cost:
                    pending.append(following)
                else:
                    pending.appendleft(following)
    return None


def main():
    rows, columns = map(int, sys.stdin.buffer.readline().split())
    scheme = [sys.stdin.buffer.readline().rstrip(b"\r\n") for _ in range(2 * rows + 1)]
    answer = minimum_passages(rows, columns, scheme)
    print("Death" if answer is None else answer)


if __name__ == "__main__":
    main()
