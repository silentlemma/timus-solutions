import sys


def sign(v):
    return (v > 0) - (v < 0)


def main():
    ax, ay, bx, by, cx, cy, dx, dy = (int(w) for w in sys.stdin.read().split())
    # both walks stay in the boxes of their ends, so the shared part lies in
    # the overlap of the two boxes
    width = min(max(ax, bx), max(cx, dx)) - max(min(ax, bx), min(cx, dx))
    height = min(max(ay, by), max(cy, dy)) - max(min(ay, by), min(cy, dy))
    if width < 0 or height < 0:
        print(0)
        return
    # walks rising the same way can share a staircase across the overlap, while
    # one rising and one falling share only one straight piece
    first = sign(bx - ax) * sign(by - ay)
    second = sign(dx - cx) * sign(dy - cy)
    print(max(width, height) if first * second < 0 else width + height)


main()
