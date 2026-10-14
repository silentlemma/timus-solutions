import sys

# the moves along each axis: (decrease, increase)
AXES = (("l", "r"), ("d", "u"), ("b", "f"))


def main():
    data = sys.stdin.read().split()
    dims = len(AXES)
    sizes = [int(x) for x in data[:dims]]
    program = data[dims] if len(data) > dims else ""
    total = 1
    for size, (down, up) in zip(sizes, AXES):
        # each move keeps neighbouring starts at most one apart and in
        # order, so the finishes fill the range between the extreme starts
        low, high = 1, size
        for step in program:
            if step == up:
                low, high = min(low + 1, size), min(high + 1, size)
            elif step == down:
                low, high = max(low - 1, 1), max(high - 1, 1)
        total *= high - low + 1
    print(total)


main()
