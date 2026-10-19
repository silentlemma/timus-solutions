import sys

POINTS = 5
END = POINTS - 1
FORBIDDEN_LAST = 2
MIDDLE_SUM = END * (END - 1) // 2


def solve(distance):
    best_cost = -1
    best_route = []
    for first in range(1, END):
        for last in range(1, END):
            if first == last or last == FORBIDDEN_LAST:
                continue
            middle = MIDDLE_SUM - first - last
            route = [0, first, middle, last, END]
            cost = sum(distance[a][b] for a, b in zip(route, route[1:]))
            if best_cost < 0 or cost < best_cost:
                best_cost, best_route = cost, route
    return best_cost, best_route


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    distance = [[next(tokens) for _ in range(POINTS)] for _ in range(POINTS)]
    cost, route = solve(distance)
    print(cost)
    print(*(point + 1 for point in route))
