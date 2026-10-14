import sys

WIDTH = 4


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    nums = data[2 : 2 + n]
    height = -(-n // k)  # the fewest rows that hold n numbers in k columns
    lines = []
    for row in range(height):
        # column c holds the numbers c * height ... c * height + height - 1
        cells = [nums[c * height + row] for c in range(k) if c * height + row < n]
        lines.append("".join(str(int(x)).rjust(WIDTH) for x in cells))
    print("\n".join(lines))


main()
