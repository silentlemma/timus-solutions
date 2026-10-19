import sys

ALICE, DRAW, BOB = 1, 0, -1


def winner(top, bottom):
    # the colour of a strip that shows a single colour on both sides, if any
    for colour, result in (("A", ALICE), ("B", BOB)):
        if top.count(colour) == len(top) and bottom.count(colour) == len(bottom):
            return result
    return None


def play(top, bottom, alice):
    # the result of optimal play from this strip with this player to move
    n = len(top)
    if n % 2:
        return DRAW
    half = n // 2
    # folding brings the right half over or under the left one; the faces that
    # end up inside are hidden
    folds = ((top[:half], top[half:][::-1]), (bottom[half:][::-1], bottom[:half]))
    best = None
    for new_top, new_bottom in folds:
        result = winner(new_top, new_bottom)
        if result is None:
            result = play(new_top, new_bottom, not alice)
        if best is None or (result > best if alice else result < best):
            best = result
        if best == (ALICE if alice else BOB):
            break
    return best


def main():
    data = sys.stdin.read().split()
    result = play(data[1], data[2], True)
    print({ALICE: "Alice", DRAW: "Draw", BOB: "Bob"}[result])


main()
