import random
import sys

MAX_SIDE = 250


def drawing(rows, columns, inside, perimeter, first, second, randomizer):
    result = []
    for r in range(2 * rows + 1):
        line = []
        for c in range(2 * columns + 1):
            if r % 2 == 0 and c % 2 == 0:
                line.append("+")
            elif r % 2 and c % 2:
                line.append(" ")
            else:
                boundary = r in (0, 2 * rows) or c in (0, 2 * columns)
                probability = perimeter if boundary else inside
                line.append(
                    "."
                    if randomizer.random() < probability
                    else "-"
                    if r % 2 == 0
                    else "|"
                )
        result.append(line)
    for point, label in ((first, "1"), (second, "2")):
        result[2 * point[0] + 1][2 * point[1] + 1] = label
    return result


def main():
    randomizer = random.Random(int(sys.argv[1]))
    mode = int(sys.argv[2])
    rows = columns = MAX_SIDE
    first, second = (124, 124), (124, 125)
    if mode == 1:
        rows, columns = randomizer.randint(2, 5), randomizer.randint(2, 5)
        first = randomizer.randrange(rows), randomizer.randrange(columns)
        options = [
            (r, c)
            for r in range(rows)
            for c in range(columns)
            if (r, c) != first and max(abs(r - first[0]), abs(c - first[1])) <= 1
        ]
        second = randomizer.choice(options)
        grid = drawing(rows, columns, 0.6, 0.5, first, second, randomizer)
    elif mode == 2:
        grid = drawing(rows, columns, 0.72, 0.5, first, second, randomizer)
    elif mode in (3, 4, 5):
        grid = drawing(
            rows, columns, 1, 1 if mode == 5 else 0, first, second, randomizer
        )
        if mode == 4:
            grid[0][1] = "."
    elif mode in (6, 7):
        rows, columns = (2, MAX_SIDE) if mode == 6 else (MAX_SIDE, 2)
        first, second = ((0, 124), (0, 125)) if mode == 6 else ((124, 0), (125, 0))
        grid = drawing(rows, columns, 1, 0, first, second, randomizer)
        grid[0][1] = "."
    elif mode == 8:
        grid = drawing(rows, columns, 0, 0, first, second, randomizer)
        for column in range(columns + 1):
            grid[2 * first[0] + 1][2 * column] = "."
    elif mode == 9:
        rows = columns = 2
        first, second = (0, 0), (0, 1)
        grid = drawing(rows, columns, 1, 0, first, second, randomizer)
        grid[0][1] = "."
    elif mode == 10:
        rows, columns = 3, 4
        lines = [
            "+.+-+-+-+",
            "| . .1. |",
            "+-+-+-+.+",
            "| .2. . |",
            "+.+.+.+-+",
            "| . | | |",
            "+.+.+-+-+",
        ]
        grid = [list(line.translate(str.maketrans("12", "21"))) for line in lines]
    elif mode == 11:
        rows, columns = 20, 25
        grid = drawing(rows, columns, 0.65, 0.5, (10, 12), (10, 13), randomizer)
    else:
        grid = drawing(rows, columns, 0.18, 0.4, first, second, randomizer)
    assert 2 <= rows <= MAX_SIDE and 2 <= columns <= MAX_SIDE
    assert len(grid) == 2 * rows + 1 and all(
        len(line) == 2 * columns + 1 for line in grid
    )
    print(rows, columns)
    print("\n".join("".join(line) for line in grid))


if __name__ == "__main__":
    main()
