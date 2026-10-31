import sys

MAX_COORD = 10**9
COORD_BITS = 31
INDEX_BITS = 14
INDEX_MASK = (1 << INDEX_BITS) - 1


def main():
    source = sys.stdin.buffer
    n = int(source.readline())
    cities = []
    for index in range(1, n + 1):
        x, y = map(int, source.readline().split())
        # each shifted coordinate fits 31 bits, index fits 14; integer sort is (x,y) sort.
        cities.append((((x + MAX_COORD) << COORD_BITS) | (y + MAX_COORD)) << INDEX_BITS | index)
    cities.sort()
    write = sys.stdout.write
    for i in range(0, n, 2):
        write(f"{cities[i] & INDEX_MASK} {cities[i + 1] & INDEX_MASK}\n")


main()
