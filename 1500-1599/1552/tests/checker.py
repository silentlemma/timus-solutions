"""Checker: a program of only > < + - . that prints the string on the
brainfuck machine (30000 byte cells, both wrapping around) and is as short
as the expected one."""

import sys

MEMORY = 30000
BYTE = 256


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    text = open(source).read().split()[0]
    want = open(expected).read().strip()
    got = open(output).read().strip()
    if set(got) - set("<>+-."):
        fail("the program has other characters")
    if len(got) != len(want):
        fail("%d commands, expected %d" % (len(got), len(want)))
    cells = [0] * MEMORY
    p = 0
    printed = []
    for c in got:
        if c == ">":
            p = (p + 1) % MEMORY
        elif c == "<":
            p = (p - 1) % MEMORY
        elif c == "+":
            cells[p] = (cells[p] + 1) % BYTE
        elif c == "-":
            cells[p] = (cells[p] - 1) % BYTE
        else:
            printed.append(chr(cells[p]))
    if "".join(printed) != text:
        fail("the program prints something else")


main()
