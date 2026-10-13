import sys


def slides_up(rows):
    """The black piece can slide up: no white cell above a black one."""
    for col in zip(*rows):
        seen_white = False
        for c in col:
            if c == "0":
                seen_white = True
            elif seen_white:
                return False
    return True


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = data[1 : n + 1]
    # a sliding direction for either piece is the opposite one for the
    # other; a diagonal slide works only if both of its axis slides do, so
    # trying the four axis directions for the black piece is enough
    up, down = grid, grid[::-1]
    left = ["".join(col) for col in zip(*grid)]
    right = left[::-1]
    views = [up, down, left, right]
    print("Yes" if any(slides_up(v) for v in views) else "No")


main()
