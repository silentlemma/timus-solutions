import sys


def main():
    n = int(sys.stdin.buffer.read())
    write = sys.stdout.write
    write("(" * (n - 1))
    prefix = ""
    for i in range(1, n + 1):
        # each sine extends the opening part of the previous one, and the pieces
        # are written as they are made
        # sin(1-sin(2+sin(3-...sin(n)...))): the sign before i is minus for even i
        if i > 1:
            prefix += "-" if i % 2 == 0 else "+"
        prefix += "sin(" + str(i)
        write(prefix + ")" * i + "+" + str(n - i + 1))
        if i < n:
            write(")")
    write("\n")


main()
