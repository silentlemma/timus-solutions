import sys


DIVISOR_THREE = 3
BATCH_SIZE = 1024


def main():
    size = int(input())
    if size % 2 == 0 or size % DIVISOR_THREE == 0:
        print("No")
        return

    # For odd n the residues 2i mod n are the even indices, then the odd ones.
    write = sys.stdout.write
    write("Yes\n")
    for first in (1, 2):
        for start in range(first, size + 1, 2 * BATCH_SIZE):
            end = min(size + 1, start + 2 * BATCH_SIZE)
            if first != 1 or start != 1:
                write(" ")
            write(" ".join(map(str, range(start, end, 2))))
    write("\n")


if __name__ == "__main__":
    main()
