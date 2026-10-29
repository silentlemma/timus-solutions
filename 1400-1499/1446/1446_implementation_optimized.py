import sys

HOUSES = (b"Slytherin", b"Hufflepuff", b"Gryffindor", b"Ravenclaw")


def main():
    # the lines are read as bytes, and every house gathers its names in one
    # bytearray that is written out as it is
    input_stream = sys.stdin.buffer
    n = int(input_stream.readline())
    lists = {house: bytearray() for house in HOUSES}
    for _ in range(n):
        # names keep their inner spaces, so only the line break is dropped
        name = input_stream.readline().rstrip(b"\r\n")
        house = input_stream.readline().strip()
        lists[house].extend(name)
        lists[house].append(ord("\n"))
    output = sys.stdout.buffer
    for index, house in enumerate(HOUSES):
        if index:
            output.write(b"\n")
        output.write(house + b":\n")
        output.write(lists[house])


main()
