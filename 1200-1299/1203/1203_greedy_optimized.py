import sys
from array import array

TIME = 30000
INPUT_BUFFER_SIZE = 16384


# the input is read in 16 KB blocks and parsed lazily, and the latest
# starts are an array of 16-bit numbers: times are at most 30000
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
    # the latest start among the talks that end at each minute
    latest = array("H", [0]) * (TIME + 1)
    for start, end in zip(values, values):
        if start > latest[end]:
            latest[end] = start
    # take the talk that ends first among those starting after the last one
    count, last = 0, 0
    for end, start in enumerate(latest):
        if start > last:
            count += 1
            last = end
    print(count)


main()
