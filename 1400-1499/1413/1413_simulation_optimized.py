import math
import sys

STOP = b"0"
CHUNK_SIZE = 8192
HALF = math.sqrt(1 / 2)  # each axis of a diagonal jump
# the numeric keypad: the jump of each key in steps east and north
DX = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
DY = [0, -1, -1, -1, 0, 0, 0, 1, 1, 1]


def main():
    # fixed chunks bound storage independently of the million-key input limit.
    counts = [0] * len(DX)
    stopped = False
    while chunk := sys.stdin.buffer.read(CHUNK_SIZE):
        if stopped:
            continue
        stop = chunk.find(STOP)
        if stop >= 0:
            chunk = chunk[:stop]
            stopped = True
        for key in range(1, len(DX)):
            counts[key] += chunk.count(str(key).encode())
    # straight jumps add whole metres, diagonal ones 1/sqrt(2) on each axis
    straight = [0, 0]
    diagonal = [0, 0]
    for key, times in enumerate(counts):
        part = diagonal if DX[key] and DY[key] else straight
        part[0] += DX[key] * times
        part[1] += DY[key] * times
    x = straight[0] + diagonal[0] * HALF
    y = straight[1] + diagonal[1] * HALF
    print("%.10f %.10f" % (x, y))


main()
