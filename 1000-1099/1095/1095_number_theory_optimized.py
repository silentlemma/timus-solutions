from sys import stdin, stdout

DIVISOR = 7
KEY = (b"1", b"2", b"3", b"4")
PLACE = 10 ** len(KEY)
# One permutation for each remainder from 0 to 6.
ORDERS = (b"3241", b"1324", b"1234", b"2341", b"1243", b"1342", b"2134")


def rearrange(number):
    for digit in KEY:
        number = number.replace(digit, b"", 1)
    head = number.replace(b"0", b"")
    remainder = (-int(head or b"0") * PLACE) % DIVISOR
    return head + ORDERS[remainder] + b"0" * (len(number) - len(head))


def main():
    source = stdin.buffer
    output = stdout.buffer
    for _ in range(int(source.readline())):
        output.write(rearrange(source.readline().strip()) + b"\n")


if __name__ == "__main__":
    main()
