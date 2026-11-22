from math import isqrt
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


DISCRIMINANT_FACTOR = 8
OUTPUT_SIZE = 4096


def main():
    values = numbers()
    count = next(values)
    answer = bytearray()
    for _ in range(count):
        discriminant = DISCRIMINANT_FACTOR * (next(values) - 1) + 1
        root = isqrt(discriminant)
        answer.extend(b"1 " if root * root == discriminant else b"0 ")
        if len(answer) >= OUTPUT_SIZE:
            write(1, answer)
            answer.clear()
    if answer:
        answer[-1] = ord("\n")
        write(1, answer)
    else:
        write(1, b"\n")
    _exit(0)


main()
