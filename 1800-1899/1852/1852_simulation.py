import sys
from itertools import product
from math import gcd

# the outward normal of every face
FACES = {"U": (0, 1, 0), "D": (0, -1, 0), "L": (-1, 0, 0),
         "R": (1, 0, 0), "F": (0, 0, 1), "B": (0, 0, -1)}
BYTES = 256
DIMENSIONS = 3


def turn(v, a, sign):
    # a quarter turn of v about the axis a: counter-clockwise seen from the
    # tip of a for sign 1, clockwise for sign -1
    cross = (a[1] * v[2] - a[2] * v[1], a[2] * v[0] - a[0] * v[2], a[0] * v[1] - a[1] * v[0])
    along = sum(x * y for x, y in zip(a, v))
    return tuple(sign * c + x * along for c, x in zip(cross, a))


def main():
    moves = sys.stdin.read().split()[0]
    # a sticker is a cubie position with every coordinate in -1..1 and the
    # outward normal of a face that cubie touches
    stickers = [(p, n) for p in product((-1, 0, 1), repeat=DIMENSIONS) for n in FACES.values()
                if sum(x * y for x, y in zip(p, n)) == 1]
    index = {s: i for i, s in enumerate(stickers)}
    # the place every sticker moves to under each letter, as a byte table
    tables = {}
    for name, a in FACES.items():
        for letter, sign in ((name, 1), (name.lower(), -1)):
            table = bytearray(range(BYTES))
            for i, (p, n) in enumerate(stickers):
                if sum(x * y for x, y in zip(p, a)) == 1:
                    table[i] = index[(turn(p, a, sign), turn(n, a, sign))]
            tables[letter] = bytes(table)
    # where each sticker ends up after the whole sequence
    place = bytes(range(len(stickers)))
    for c in moves:
        place = place.translate(tables[c])
    # the sequence returns the cube after the lcm of the cycle lengths
    order, seen = 1, [False] * len(stickers)
    for start in range(len(stickers)):
        length, i = 0, start
        while not seen[i]:
            seen[i] = True
            i = place[i]
            length += 1
        if length:
            order = order * length // gcd(order, length)
    print(order - 1)


main()
