import sys
from array import array

LARGEST = 25000
INPUT_BUFFER_SIZE = 4096


# the numbers are read in 4 KB blocks instead of splitting the whole input
def numbers():
    pending = b""
    while True:
        block = sys.stdin.buffer.read(INPUT_BUFFER_SIZE)
        if not block:
            if pending:
                yield int(pending)
            return
        tokens = (pending + block).split()
        pending = tokens.pop() if block[-1] > ord(" ") else b""
        yield from map(int, tokens)


def main():
    values = numbers()
    next(values)
    # counting each value is a sort in descending order, and printing the
    # conjugate partition twice gives back the sorted array; at most 25 000
    # numbers, so 16-bit counters are enough
    count = array("H", [0]) * (LARGEST + 1)
    for value in values:
        count[value] += 1
    write = sys.stdout.write
    for value in range(LARGEST, 0, -1):
        if count[value]:
            # each value is formatted once and repeated count times
            write((str(value) + "\n") * count[value])


main()
