import sys

CLASSES = 4  # houses by the parities of x and y
CANDIDATES_PER_PLACE = 5  # 5n names for n places


def main():
    data = [int(w) for w in sys.stdin.buffer.read().split()]
    n = data[0]
    groups = [[] for _ in range(CLASSES)]
    for i in range(CANDIDATES_PER_PLACE * n):
        x, y = data[1 + 2 * i], data[2 + 2 * i]
        groups[2 * (x % 2) + y % 2].append(i + 1)
    # two houses with the same parities differ by even dx and dy, so the
    # middle of their segment is a lattice point; 5n houses in 4 classes
    # leave one class with at least n of them, so the army always exists
    best = max(groups, key=len)
    print("OK")
    print(" ".join(map(str, best[:n])))


main()
