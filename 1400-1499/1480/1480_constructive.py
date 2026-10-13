import sys


def main():
    n = int(sys.stdin.read())
    # a chessboard: the large numbers go down on one colour and the small
    # ones up on the other, both in reading order
    big, small = n * n, 1
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append(big)
                big -= 1
            else:
                row.append(small)
                small += 1
        rows.append(" ".join(map(str, row)))
    print(n * n + n // 2 + 1)
    print("\n".join(rows))


main()
