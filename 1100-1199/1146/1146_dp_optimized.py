import sys
from array import array
from operator import add

INPUT_BUFFER_SIZE = 4096


# the input is read in 4 KB blocks and parsed lazily, and each row is an
# array of bytes, since every value is between -127 and 127
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
    n = next(values)
    grid = [array("b", (next(values) for _ in range(n))) for _ in range(n)]
    best = grid[0][0]
    for top in range(n):
        # column sums of the rows from top to bottom, then the best run of
        # neighbouring columns by Kadane's scan
        cols = [0] * n
        for bottom in range(top, n):
            # the row is added to the column sums by map instead of a Python loop
            cols = list(map(add, cols, grid[bottom]))
            run = 0
            for value in cols:
                run = value if run < 0 else run + value
                if run > best:
                    best = run
    print(best)


main()
