"""Checker: the rectangles lie inside the picture, cover only black pixels,
together cover all of them, and there are as many as in the expected
answer, which is the least number."""

import sys

CORNERS = 4  # numbers per rectangle


def main():
    path_in, expected, output = sys.argv[1:4]
    data = open(path_in).read().split()
    n, m = int(data[0]), int(data[1])
    rows = data[2 : 2 + n]
    want = int(open(expected).read().split()[0])
    words = open(output).read().split()
    if not words or len(words) != 1 + CORNERS * int(words[0]):
        print("malformed answer")
        sys.exit(1)
    count = int(words[0])
    if count != want:
        print("%d rectangles, the least number is %d" % (count, want))
        sys.exit(1)
    covered = [[False] * m for _ in range(n)]
    for i in range(count):
        a, b, c, d = (int(x) for x in words[1 + CORNERS * i : 1 + CORNERS * (i + 1)])
        top, bottom = min(a, c), max(a, c)
        left, right = min(b, d), max(b, d)
        if top < 1 or left < 1 or bottom > n or right > m:
            print("rectangle %d leaves the picture" % (i + 1))
            sys.exit(1)
        for r in range(top - 1, bottom):
            for col in range(left - 1, right):
                if rows[r][col] != "1":
                    print("rectangle %d covers a white pixel" % (i + 1))
                    sys.exit(1)
                covered[r][col] = True
    for r in range(n):
        for col in range(m):
            if rows[r][col] == "1" and not covered[r][col]:
                print("pixel %d %d is not covered" % (r + 1, col + 1))
                sys.exit(1)


if __name__ == "__main__":
    main()
