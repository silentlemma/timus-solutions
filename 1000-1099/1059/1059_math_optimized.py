import sys


def write_expression(degree, write):
    write(b"0\n")
    # Each Horner step multiplies by X and adds the next coefficient.
    for index in range(1, degree + 1):
        write(b"X\n*\n%d\n+\n" % index)


def main():
    degree = int(sys.stdin.buffer.read())
    write_expression(degree, sys.stdout.buffer.write)


if __name__ == "__main__":
    main()
