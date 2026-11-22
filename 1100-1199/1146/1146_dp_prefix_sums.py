import os
import sys
from array import array
from operator import add, sub

INPUT_BUFFER_SIZE = 512


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


def finish(answer):
    print(answer)
    sys.stdout.flush()
    os._exit(0)


def solve():
    values = numbers()
    n = next(values)
    # Each vertical prefix is within [-12700, 12700] because n <= 100.
    prefix = [array("h", [0]) * n]
    positive = [0]
    best = None
    for _ in range(n):
        row = [next(values) for _ in range(n)]
        largest = max(row)
        if best is None or largest > best:
            best = largest
        positive.append(positive[-1] + sum(value for value in row if value > 0))
        prefix.append(array("h", map(add, prefix[-1], row)))
    # Matrix prefixes are complete; release the final token batch and row.
    del row, values
    if best <= 0:
        finish(best)
    for top in range(n):
        # Even selecting every positive cell in the remaining rows cannot win.
        if positive[n] - positive[top] <= best:
            break
        first = prefix[top]
        for end in range(n, top, -1):
            if positive[end] - positive[top] <= best:
                break
            run = 0
            for value in map(sub, prefix[end], first):
                run = value if run < 0 else run + value
                if run > best:
                    best = run
    finish(best)


solve()
