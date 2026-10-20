import sys

ONE = ord("1")


def main():
    x, y = sys.stdin.buffer.read().split()
    size = max(len(x), len(y))
    x = x.rjust(size, b"0")
    y = y.rjust(size, b"0")

    propagating = 0
    longest = 0
    for a, b in zip(x, y):
        if a != b:
            propagating += 1
        else:
            # A common one starts a carry through the differing bits above it.
            if a == ONE and propagating + 1 > longest:
                longest = propagating + 1
            propagating = 0
    # Include the initial call and the final call with a zero second argument.
    print(longest + 2)


if __name__ == "__main__":
    main()
