import sys

CYCLE_CUT = 3  # a cycle on s vertices has path(s - 1) + path(s - 3) sets


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    rows = data[1:1 + n]
    # a working group is a clique of friends, that is an independent set of
    # the graph of non-friends; every group plus the empty one is a day, so
    # the day of rusting is the number of independent sets, empty included
    enemy = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and rows[i][j] == "0":
                enemy[i] |= 1 << j
    # independent sets of a path and of a cycle on s vertices
    path = [1, 2]
    for s in range(2, n + 1):
        path.append(path[-1] + path[-2])
    memo = {}

    def count(mask):
        if mask == 0:
            return 1
        if mask in memo:
            return memo[mask]
        # split into connected parts, which multiply
        low = mask & -mask
        part, frontier = low, low
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            grow = enemy[bit.bit_length() - 1] & mask & ~part
            part |= grow
            frontier |= grow
        if part != mask:
            result = count(part) * count(mask & ~part)
            memo[mask] = result
            return result
        size = bin(mask).count("1")
        pivot, most, ends = -1, -1, False
        rest = mask
        while rest:
            bit = rest & -rest
            rest ^= bit
            v = bit.bit_length() - 1
            degree = bin(enemy[v] & mask).count("1")
            ends = ends or degree == 1
            if degree > most:
                pivot, most = v, degree
        if most == size - 1 and all(bin(enemy[v] & mask).count("1") == size - 1
                                    for v in range(n) if mask >> v & 1):
            result = size + 1  # all pairs are enemies: the empty set or one robot
        elif most <= 2:
            result = path[size] if ends else path[size - 1] + path[size - CYCLE_CUT]
        else:
            # branch on a vertex of most enemies: leave it out, or take it
            # and drop all its enemies
            bit = 1 << pivot
            result = count(mask & ~bit) + count(mask & ~(enemy[pivot] | bit))
        memo[mask] = result
        return result

    print(count((1 << n) - 1))


main()
