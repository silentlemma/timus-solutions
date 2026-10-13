import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, s = int(data[0]), int(data[1])
    c = [int(x) for x in data[2 : 2 + n]]
    rook = n * (s - 1)
    if n == 1:
        # in one dimension a bishop moves exactly like a rook
        print(rook)
        return
    # t bishop steps need room t on the chosen side of every coordinate
    both = [0] * s  # both[m]: coordinates with room m on each side
    for x in c:
        both[min(s - x, x - 1)] += 1
    reach = min(max(s - x, x - 1) for x in c)  # beyond this some coordinate has no room
    count = [0] * (n + 1)  # count[k]: lengths t with 2^k directions
    k = n - both[0]
    for t in range(1, reach + 1):
        count[k] += 1
        k -= both[t]
    ways = 0
    for k in range(n, -1, -1):
        ways = 2 * ways + count[k]
    print(rook + ways)


main()
