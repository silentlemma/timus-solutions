from collections import deque
from os import _exit, read, write

INPUT_SIZE = 4096
WHITESPACE = ord(" ")


def numbers():
    pending = b""
    while block := read(0, INPUT_SIZE):
        fields = (pending + block).split()
        pending = fields.pop() if block[-1] > WHITESPACE else b""
        yield from map(int, fields)
    if pending:
        yield int(pending)


INDEX_BITS = 15
INDEX_MASK = (1 << INDEX_BITS) - 1
OUTPUT_BATCH = 512


def main():
    values = numbers()
    width = next(values)
    window = deque()
    answers = []
    for index, value in enumerate(values):
        if value < 0:
            break
        if window and (window[0] & INDEX_MASK) <= index - width:
            window.popleft()
        # N<=25000 leaves every index in15 bits. Integer order compares value
        # first, then index: equal older values are safely replaced by this one.
        packed = (value << INDEX_BITS) | index
        while window and window[-1] <= packed:
            window.pop()
        window.append(packed)
        if index + 1 >= width:
            answers.append(str(window[0] >> INDEX_BITS))
            if len(answers) == OUTPUT_BATCH:
                write(1, ("\n".join(answers) + "\n").encode())
                answers.clear()
    if answers:
        write(1, ("\n".join(answers) + "\n").encode())
    _exit(0)


main()
