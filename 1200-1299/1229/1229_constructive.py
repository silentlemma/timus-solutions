import sys


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    first = [data[2 + i * m : 2 + (i + 1) * m] for i in range(n)]
    second = [[0] * m for _ in range(n)]
    label = 0
    # cover every 2 x 2 block with two bricks: lying flat unless a brick of
    # the first layer fills its top or bottom row, and then standing, which
    # no first-layer brick can match, as that brick holds a cell of each column
    for i in range(0, n, 2):
        for j in range(0, m, 2):
            flat = first[i][j] != first[i][j + 1] and first[i + 1][j] != first[i + 1][j + 1]
            a, b = label + 1, label + 2
            label = b
            if flat:
                second[i][j] = second[i][j + 1] = a
                second[i + 1][j] = second[i + 1][j + 1] = b
            else:
                second[i][j] = second[i + 1][j] = a
                second[i][j + 1] = second[i + 1][j + 1] = b
    print("\n".join(" ".join(map(str, row)) for row in second))


main()
