"""Random frames drawn on the screen; a seed, the frame count and the maximal
side. picture() gives the screen as cp437 bytes; the test is printed in UTF-8."""

import random
import sys

WIDTH, HEIGHT = 50, 20
MIN_SIDE = 2
EMPTY = ord(".")
UPPER_LEFT, UPPER_RIGHT, LOWER_LEFT, LOWER_RIGHT = 218, 191, 192, 217
VERTICAL, HORIZONTAL = 179, 196


def draw(screen, x, y, side):
    last = side - 1
    for i in range(1, last):
        screen[y][x + i] = screen[y + last][x + i] = HORIZONTAL
        screen[y + i][x] = screen[y + i][x + last] = VERTICAL
    screen[y][x] = UPPER_LEFT
    screen[y][x + last] = UPPER_RIGHT
    screen[y + last][x] = LOWER_LEFT
    screen[y + last][x + last] = LOWER_RIGHT


def picture(frames):
    screen = [bytearray([EMPTY] * WIDTH) for _ in range(HEIGHT)]
    for x, y, side in frames:
        draw(screen, x, y, side)
    return b"".join(bytes(row) + b"\n" for row in screen)


def main():
    seed, count, max_side = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    frames = []
    for _ in range(count):
        side = rng.randint(MIN_SIDE, min(max_side, HEIGHT))
        frames.append((rng.randint(0, WIDTH - side), rng.randint(0, HEIGHT - side), side))
    sys.stdout.buffer.write(picture(frames).decode("cp437").encode("utf-8"))


if __name__ == "__main__":
    main()
