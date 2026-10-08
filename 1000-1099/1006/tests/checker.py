"""Checker: at most MAX_FRAMES frames inside the screen that, drawn in the given
order on an empty screen, give exactly the input picture."""

import sys

from gen import HEIGHT, MIN_SIDE, WIDTH, picture

MAX_FRAMES = 2000
TOKENS_PER_FRAME = 3


def main():
    inp, _, output = sys.argv[1:4]
    rows = open(inp, "rb").read().replace(b"\r", b"").split(b"\n")[:HEIGHT]
    want = b"".join(row + b"\n" for row in rows)
    try:
        tokens = [int(x) for x in open(output).read().split()]
    except ValueError:
        print("non-integer token")
        sys.exit(1)
    if not tokens or not 0 <= tokens[0] <= MAX_FRAMES:
        print("bad frame count")
        sys.exit(1)
    count = tokens[0]
    if len(tokens) != 1 + TOKENS_PER_FRAME * count:
        print("expected %d frames" % count)
        sys.exit(1)
    frames = []
    for i in range(count):
        x, y, side = tokens[1 + TOKENS_PER_FRAME * i : 1 + TOKENS_PER_FRAME * (i + 1)]
        if side < MIN_SIDE or x < 0 or y < 0 or x + side > WIDTH or y + side > HEIGHT:
            print("frame %d (%d %d %d) is not on the screen" % (i + 1, x, y, side))
            sys.exit(1)
        frames.append((x, y, side))
    if picture(frames) != want:
        print("the frames give another picture")
        sys.exit(1)


main()
