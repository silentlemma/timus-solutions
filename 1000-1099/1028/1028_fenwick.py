import sys

MAX_COORD = 32000


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = data[1 : 1 + 2 * n : 2]
    # stars come by y, then x: the level of a star is the number of stars
    # already seen with x not greater than its own; a Fenwick tree counts them
    tree = [0] * (MAX_COORD + 2)
    count = [0] * n
    top = MAX_COORD + 1
    for x in xs:
        j = int(x) + 1
        start, level = j, 0
        while j > 0:
            level += tree[j]
            j &= j - 1
        count[level] += 1
        j = start
        while j <= top:
            tree[j] += 1
            j += j & -j
    sys.stdout.write("\n".join(map(str, count)) + "\n")


main()
