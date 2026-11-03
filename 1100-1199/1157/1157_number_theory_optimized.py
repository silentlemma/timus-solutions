import sys

LIMIT = 10000


def main():
    before, after, added = map(int, sys.stdin.buffer.read().split())
    shapes = bytearray(LIMIT + 1)
    side = 1
    # Every rectangle has one unique pair side<=other; count it once.
    while side * side <= LIMIT:
        for tiles in range(side * side, LIMIT + 1, side):
            shapes[tiles] += 1
        side += 1
    print(
        next(
            (
                tiles
                for tiles in range(added + 1, LIMIT + 1)
                if shapes[tiles] == after and shapes[tiles - added] == before
            ),
            0,
        )
    )


main()
