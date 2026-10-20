"""Check one-command relocation and the minimum score using a separate state DP."""

import sys

STEPS = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
MAX_LENGTH = 100_000
MAX_VALUE = 1_000_000_000
INFINITY = (MAX_LENGTH + 2) * MAX_VALUE * 2
ARGUMENT_COUNT = 3


class Bad(Exception):
    pass


def reachable(source, answer):
    if source == answer:
        return True
    first = next(i for i, (a, b) in enumerate(zip(source, answer)) if a != b)
    last = len(source) - 1
    while source[last] == answer[last]:
        last -= 1
    middle = answer[first : last + 1]
    return middle in (
        source[first + 1 : last + 1] + source[first],
        source[last] + source[first:last],
    )


def minimum_score(board, n, m, source):
    def cell(x, y):
        return board[x * m + y] if 0 <= x < n and 0 <= y < m else 0

    result = INFINITY
    for moved, (dx, dy) in STEPS.items():
        x = y = 0
        plain = board[0]
        removed = inserted = done = INFINITY
        for command in source:
            # An active state has either removed or inserted the relocated command.
            inserted = min(inserted, plain + cell(x + dx, y + dy))
            done = min(done, removed + cell(x, y))
            step_x, step_y = STEPS[command]
            x += step_x
            y += step_y
            value = cell(x, y)
            next_removed = removed + cell(x - dx, y - dy)
            next_inserted = inserted + cell(x + dx, y + dy)
            done += value
            if command == moved:
                next_removed = min(next_removed, plain)
                done = min(done, inserted)
            removed, inserted = next_removed, next_inserted
            plain += value
        result = min(result, done, removed + cell(x, y))
    return result


def check(source_path, expected_path, output_path):
    with open(source_path, encoding="utf-8") as stream:
        data = stream.read().split()
    n, m = map(int, data[:2])
    board = list(map(int, data[2:-1]))
    source = data[-1]
    with open(output_path, encoding="utf-8") as stream:
        tokens = stream.read().split()
    if len(tokens) != 1:
        raise Bad("expected one program")
    answer = tokens[0]
    if len(answer) != len(source) or any(c not in STEPS for c in answer):
        raise Bad("incorrect program length or command")
    if not reachable(source, answer):
        raise Bad("the program is not one command relocation")
    x = y = 0
    score = board[0]
    for command in answer:
        dx, dy = STEPS[command]
        x += dx
        y += dy
        if 0 <= x < n and 0 <= y < m:
            score += board[x * m + y]
    optimum = minimum_score(board, n, m, source)
    if score != optimum:
        raise Bad("score %d is not the minimum %d" % (score, optimum))


def main():
    if len(sys.argv) != ARGUMENT_COUNT + 1:
        print("usage: checker.py INPUT EXPECTED OUTPUT")
        sys.exit(1)
    try:
        check(*sys.argv[1:])
    except (Bad, OSError, UnicodeError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
