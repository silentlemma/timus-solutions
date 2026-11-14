import sys

TICKET = 4


def meeting_stop(neighbors, paying, budgets):
    count = len(neighbors)
    possible = (1 << count) - 1
    costs = [0] * count
    starts = sorted((budget, start) for start, budget in enumerate(budgets) if budget >= 0)
    for budget, start in starts:
        frontier = reached = 1 << start
        riders = paying[start]
        for rides in range(budget + 1):
            if rides and riders:
                fare = rides * riders * TICKET
                remaining = frontier & possible
                while remaining:
                    bit = remaining & -remaining
                    costs[bit.bit_length() - 1] += fare
                    remaining ^= bit
            if rides == budget or possible & ~reached == 0:
                break
            following = 0
            while frontier:
                bit = frontier & -frontier
                following |= neighbors[bit.bit_length() - 1]
                frontier ^= bit
            frontier = following & ~reached
            if frontier == 0:
                break
            reached |= frontier
        possible &= reached
        if not possible:
            return None

    best_stop = (possible & -possible).bit_length() - 1
    while possible:
        bit = possible & -possible
        stop = bit.bit_length() - 1
        if costs[stop] < costs[best_stop]:
            best_stop = stop
        possible ^= bit
    return best_stop + 1, costs[best_stop]


def main():
    values = (int(field) for line in sys.stdin.buffer for field in line.split())
    count, route_count = next(values), next(values)
    neighbors = [0] * count
    for _ in range(route_count):
        route = 0
        for _ in range(next(values)):
            route |= 1 << (next(values) - 1)
        remaining = route
        while remaining:
            bit = remaining & -remaining
            neighbors[bit.bit_length() - 1] |= route
            remaining ^= bit
    paying = [0] * count
    budgets = [-1] * count
    for _ in range(next(values)):
        money, start, pass_holder = next(values), next(values) - 1, next(values)
        if budgets[start] < 0:
            budgets[start] = count - 1
        if not pass_holder:
            paying[start] += 1
            budgets[start] = min(budgets[start], money // TICKET)
    result = meeting_stop(neighbors, paying, budgets)
    if result is None:
        print(0)
    else:
        print(*result)


if __name__ == "__main__":
    main()
