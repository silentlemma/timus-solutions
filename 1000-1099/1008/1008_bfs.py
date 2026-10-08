import sys

STEPS = ((1, 0, "R"), (0, 1, "T"), (-1, 0, "L"), (0, -1, "B"))
SHIFT = {letter: (dx, dy) for dx, dy, letter in STEPS}


def describe(pixels):
    """Breadth-first search from the lowest of the leftmost pixels; each line
    names the neighbours seen for the first time."""
    start = min(pixels)
    queue, seen, lines = [start], {start}, []
    for x, y in queue:
        line = ""
        for dx, dy, letter in STEPS:
            p = (x + dx, y + dy)
            if p in pixels and p not in seen:
                seen.add(p)
                queue.append(p)
                line += letter
        lines.append(line)
    return ["%d %d" % start] + [line + "," for line in lines[:-1]] + [lines[-1] + "."]


def pixel_list(start, lines):
    """Replay the same search: the lines tell which pixels it adds."""
    queue = [start]
    for (x, y), line in zip(queue, lines):
        for letter in line.rstrip(",."):
            dx, dy = SHIFT[letter]
            queue.append((x + dx, y + dy))
    return [str(len(queue))] + ["%d %d" % p for p in sorted(queue)]


def main():
    tokens = sys.stdin.read().split()
    # only the description ends with a full stop
    if tokens[-1].endswith("."):
        out = pixel_list((int(tokens[0]), int(tokens[1])), tokens[2:])
    else:
        nums = list(map(int, tokens))
        out = describe(set(zip(nums[1::2], nums[2::2])))
    print("\n".join(out))


main()
