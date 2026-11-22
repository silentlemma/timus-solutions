import os
from itertools import groupby
from sys import stdin, stdout


def main():
    read = stdin.buffer.readline
    rooms = int(read())
    dummy_bit = 1 << rooms
    edges = [0] * (rooms + 1)
    outward = [0] * rooms
    counts = []
    for room in range(rooms):
        tokens = iter(map(int, read().split()))
        degree = next(tokens)
        row = [0] * rooms
        mask = 0
        # Neighbours are sorted, so each run counts one parallel-door group.
        for neighbor, group in groupby(tokens):
            other = neighbor - 1
            doors = len(list(group))
            row[other] = doors
            if other != room and doors % 2:
                mask |= 1 << other
        if degree % 2:
            mask |= dummy_bit
            edges[rooms] |= 1 << room
        edges[room] = mask
        counts.append(row)

    # Every augmented degree is even: each greedy unused-edge walk closes.
    for start in range(rooms + 1):
        room = start
        while edges[room]:
            bit = edges[room] & -edges[room]
            other = bit.bit_length() - 1
            edges[room] ^= bit
            edges[other] ^= 1 << room
            if room < rooms:
                outward[room] |= bit
            room = other

    for room, counts_by_neighbor in enumerate(counts):
        row = bytearray()
        mask = outward[room]
        for other, doors in enumerate(counts_by_neighbor):
            if not doors:
                continue
            green = doors // 2 + ((mask >> other) & 1)
            row.extend(b"G " * green)
            row.extend(b"Y " * (doors - green))
        if row:
            row[-1] = ord("\n")
        else:
            row.extend(b"\n")
        stdout.buffer.write(row)


main()
stdout.flush()
os._exit(0)
