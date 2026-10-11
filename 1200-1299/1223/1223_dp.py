import sys

FLOORS = 1000
# ten eggs already allow a binary search over all the floors
EGGS = 10


def main():
    # best[k][n]: the fewest drops that settle n floors with k eggs; with d
    # drops and k eggs one can tell apart reach(d, k) floors, where
    # reach(d, k) = reach(d - 1, k - 1) + reach(d - 1, k) + 1
    best = [[0] * (FLOORS + 1) for _ in range(EGGS + 1)]
    reach = [0] * (EGGS + 1)
    d = 0
    while reach[1] < FLOORS:
        d += 1
        new = [0] + [min(FLOORS, reach[k - 1] + reach[k] + 1) for k in range(1, EGGS + 1)]
        for k in range(1, EGGS + 1):
            for n in range(reach[k] + 1, new[k] + 1):
                best[k][n] = d
        reach = new
    data = sys.stdin.read().split()
    out = []
    for eggs, floors in zip(map(int, data[0::2]), map(int, data[1::2])):
        if eggs == 0 and floors == 0:
            break
        out.append(best[min(eggs, EGGS)][floors])
    print("\n".join(map(str, out)))


main()
