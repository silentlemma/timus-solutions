"""Check the verdict against the stored one and every printed seat: free,
distinct, and no two adjacent on the same side of the aisle."""

import re
import sys

LETTERS = "ABCDEF"
SIDE = 3
RIGHT_START = 6
ARGS = 4


class Bad(Exception):
    pass


def check(source, expected, output):
    data = open(source).read().split()
    n, k = int(data[0]), int(data[1])
    rows = data[2:2 + n]
    want = open(expected).read().split()
    got = open(output).read().split()
    if not got or got[0] not in ("POBEDA", "PORAZHENIE"):
        raise Bad("expected POBEDA or PORAZHENIE")
    if got[0] != want[0]:
        raise Bad("wrong verdict %s" % got[0])
    if got[0] == "PORAZHENIE":
        if len(got) != 1:
            raise Bad("extra output after PORAZHENIE")
        return
    seats = got[1:]
    if len(seats) != k:
        raise Bad("expected %d seats, got %d" % (k, len(seats)))
    places = set()
    for seat in seats:
        match = re.fullmatch(r"([1-9][0-9]*)([A-F])", seat)
        if not match:
            raise Bad("bad seat %s" % seat)
        row = int(match.group(1)) - 1
        letter = LETTERS.index(match.group(2))
        if row >= n:
            raise Bad("no row for %s" % seat)
        side, column = divmod(letter, SIDE)
        if rows[row][side * RIGHT_START + column] != ".":
            raise Bad("seat %s is taken" % seat)
        if (row, letter) in places:
            raise Bad("seat %s is repeated" % seat)
        places.add((row, letter))
    for row, letter in places:
        for other_row, other_letter in places:
            if (row, letter) == (other_row, other_letter):
                continue
            if letter // SIDE != other_letter // SIDE:
                continue
            if abs(row - other_row) <= 1 and abs(letter - other_letter) <= 1:
                raise Bad("seats %d%s and %d%s are adjacent"
                          % (row + 1, LETTERS[letter], other_row + 1, LETTERS[other_letter]))


def main():
    try:
        check(*sys.argv[1:ARGS])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
