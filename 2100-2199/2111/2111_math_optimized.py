import sys

INPUT_BUFFER_SIZE = 16384


# the input is read in 16 KB blocks and parsed lazily, so the list of all
# distances is never built
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
    total = sum(values)
    # a trip to a city with load L costs L d there and (L - d) d back; summed over
    # any order this is (sum of d)^2, so the order does not matter
    print(total * total)


main()
