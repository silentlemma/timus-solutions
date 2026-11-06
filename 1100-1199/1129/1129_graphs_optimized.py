from array import array
from sys import stdin, stdout

UNUSED = 1
OUTWARD = 2
INWARD = 3


def main():
    read = stdin.buffer.readline
    rooms = int(read())
    width = rooms + 1
    dummy = rooms
    counts = [array("I", [0]) * rooms for _ in range(rooms)]
    edges = [bytearray(width) for _ in range(width)]
    for room in range(rooms):
        row = iter(map(int, read().split()))
        degree = next(row)
        for other in row:
            counts[room][other - 1] += 1
        if degree % 2:
            edges[room][dummy] = edges[dummy][room] = UNUSED
        for other, doors in enumerate(counts[room]):
            if room != other and doors % 2:
                edges[room][other] = UNUSED

    cursor = [0] * width
    for start in range(width):
        room = start
        while True:
            other = cursor[room]
            while other < width and edges[room][other] != UNUSED:
                other += 1
            cursor[room] = other
            if other == width:
                break
            edges[room][other] = OUTWARD
            edges[other][room] = INWARD
            room = other

    for room, counts_by_neighbor in enumerate(counts):
        row = bytearray()
        for other, doors in enumerate(counts_by_neighbor):
            green = doors // 2 + (edges[room][other] == OUTWARD)
            row.extend(b"G " * green)
            row.extend(b"Y " * (doors - green))
        if row:
            row[-1] = ord("\n")
        else:
            row.extend(b"\n")
        stdout.buffer.write(row)


main()
