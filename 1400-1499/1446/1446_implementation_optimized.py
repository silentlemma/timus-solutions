import os
import sys

HOUSES = (b"Slytherin", b"Hufflepuff", b"Gryffindor", b"Ravenclaw")


def main():
    # the lines are read as bytes, and every house gathers its names in one
    # bytearray that is written out as it is
    read = sys.stdin.buffer.readline
    n = int(read())
    lists = {house: bytearray() for house in HOUSES}
    for _ in range(n):
        # names keep their inner spaces, so only the line break is dropped
        name = read().rstrip(b"\r\n")
        house = read().strip()
        lists[house].extend(name)
        lists[house].append(ord("\n"))
    output = sys.stdout.buffer
    for index, house in enumerate(HOUSES):
        if index:
            output.write(b"\n")
        output.write(house + b":\n")
        output.write(lists[house])


main()

sys.stdout.flush()
os._exit(0)
