import sys

NAME_WIDTH = 30
DATE_WIDTH = 8
LETTERS = b"ABCDEFGHIJKLM"
FIRST_PROBLEM = ord("A")
ACCEPTED = ord("o")
FAILED = ord("x")


def main():
    read = sys.stdin.buffer.readline
    write = sys.stdout.buffer.write
    n = int(read())
    border = (
        b"+" + b"-" * NAME_WIDTH + b"+" + b"-" * DATE_WIDTH + b"+" + b"-" * len(LETTERS) + b"+\n"
    )
    write(border)
    write(
        b"|"
        + b"Contest name".ljust(NAME_WIDTH)
        + b"|"
        + b"Date".ljust(DATE_WIDTH)
        + b"|"
        + LETTERS
        + b"|\n"
    )
    write(border)
    for _ in range(n):
        name = read().rstrip(b"\r\n")
        date = read().rstrip(b"\r\n")
        p, s = map(int, read().split())
        marks = bytearray(b"." * p + b" " * (len(LETTERS) - p))
        for _ in range(s):
            submit = read()
            problem = submit[0] - FIRST_PROBLEM
            # Accepted is the only allowed verdict beginning with A.
            if submit[2] == FIRST_PROBLEM:
                marks[problem] = ACCEPTED
            elif marks[problem] != ACCEPTED:
                marks[problem] = FAILED
        write(b"|" + name.ljust(NAME_WIDTH) + b"|" + date + b"|" + marks + b"|\n")
        write(border)


main()
