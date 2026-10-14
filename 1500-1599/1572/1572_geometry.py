import sys

# four times the square of the shortest longest chord of a cover of side or
# radius 1, by type: a circle's diameter, a square's side, a triangle's height
NARROWEST = [0, 16, 4, 3]
# four times the square of the longest segment in a hole: a circle's
# diameter, a square's diagonal, a triangle's side
WIDEST = [0, 16, 8, 4]


def main():
    words = iter(sys.stdin.read().split())
    kind, size = int(next(words)), int(next(words))
    hole = WIDEST[kind] * size * size
    n = int(next(words))
    covers = [(int(next(words)), int(next(words))) for _ in range(n)]
    # a cover held upright crosses the plane of the hole along parallel chords,
    # so it passes when its longest chord in some direction fits in the hole
    print(sum(NARROWEST[kind] * size * size <= hole for kind, size in covers))


main()
