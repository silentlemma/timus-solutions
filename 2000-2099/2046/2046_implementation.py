"""Wrap whole words and render a fixed timetable with exact cell padding."""

import sys

WIDTH = 10
ROWS = 4
DAYS = ("Tuesday", "Thursday", "Saturday")


def wrap(name):
    lines = [""]
    for word in name.split():
        if not lines[-1]:
            lines[-1] = word
        elif len(lines[-1]) + 1 + len(word) <= WIDTH:
            lines[-1] += " " + word
        else:
            lines.append(word)
    return lines


def render(grid):
    border = "+" + ("-" * WIDTH + "+") * len(DAYS)
    output = [border]
    for row in grid:
        height = max(1, max(map(len, row)))
        for level in range(height):
            output.append(
                "|"
                + "|".join((cell[level] if level < len(cell) else "").ljust(WIDTH) for cell in row)
                + "|"
            )
        output.append(border)
    return "\n".join(output) + "\n"


def main():
    lines = iter(sys.stdin.read().splitlines())
    n = int(next(lines))
    grid = [[[] for _ in DAYS] for _ in range(ROWS)]
    for _ in range(n):
        name = next(lines)
        day, lesson = next(lines).split()
        grid[int(lesson) - 1][DAYS.index(day)] = wrap(name)
    sys.stdout.write(render(grid))


if __name__ == "__main__":
    main()
