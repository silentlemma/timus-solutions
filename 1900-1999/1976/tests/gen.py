"""Generate large binary maps: python gen.py SEED MODE.

Modes corner, corners, center, checkerboard, diagonal, antidiagonal,
lattice, stripes, block, dense, sparse, nearly_full and bottom_row use 1000x1000 maps.
All modes contain both a base and a free cell. Output is the problem input.
"""

import random
import sys


def generate(seed, mode):
    height = width = 1000
    rng = random.Random(seed)
    cells = bytearray(b"0") * (height * width)
    if mode in ("corner", "corners", "center", "sparse"):
        if mode == "corner":
            positions = [(0, 0)]
        elif mode == "corners":
            positions = [
                (0, 0),
                (0, width - 1),
                (height - 1, 0),
                (height - 1, width - 1),
            ]
        elif mode == "center":
            positions = [(height // 2, width // 2)]
        else:
            positions = rng.sample(range(height * width), 8)
            positions = [divmod(p, width) for p in positions]
        for row, column in positions:
            cells[row * width + column] = ord("1")
    elif mode == "nearly_full":
        cells = bytearray(b"1") * (height * width)
        cells[(height // 2) * width + width // 2] = ord("0")
    elif mode == "bottom_row":
        cells[(height - 1) * width :] = b"1" * width
    elif mode == "diagonal":
        for row in range(height):
            cells[row * width + row] = ord("1")
    elif mode == "antidiagonal":
        for row in range(height):
            cells[row * width + width - 1 - row] = ord("1")
    elif mode in ("lattice", "stripes", "block", "checkerboard", "dense"):
        for row in range(height):
            for column in range(width):
                if mode == "lattice":
                    base = row % 97 == 11 and column % 113 == 17
                elif mode == "stripes":
                    base = column % 101 == 13
                elif mode == "block":
                    base = (
                        height // 4 <= row < 3 * height // 4
                        and width // 4 <= column < 3 * width // 4
                    )
                elif mode == "checkerboard":
                    base = (row + column) % 2 == 0
                else:
                    base = rng.random() < 0.37
                if base:
                    cells[row * width + column] = ord("1")
        if mode == "dense":
            cells[0], cells[-1] = ord("1"), ord("0")
    else:
        raise ValueError("unknown generation mode: " + mode)
    return height, width, bytes(cells)


def main():
    seed, mode = int(sys.argv[1]), sys.argv[2]
    height, width, cells = generate(seed, mode)
    print(height, width)
    for row in range(height):
        print(cells[row * width : (row + 1) * width].decode())


if __name__ == "__main__":
    main()
