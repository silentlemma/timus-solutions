"""Check a Hamiltonian route, its length and the independent subset-DP optimum."""

from pathlib import Path
import sys

POINTS = 5
START = 0
END = POINTS - 1
FORBIDDEN_LAST = 2
FULL = (1 << (POINTS - 2)) - 1
INFINITY = 10**9


def optimum(distance):
    dp = {(0, START): 0}
    for mask in range(FULL + 1):
        for last in range(END):
            if (mask, last) not in dp:
                continue
            for to in range(1, END):
                bit = 1 << (to - 1)
                if mask & bit:
                    continue
                key = mask | bit, to
                value = dp[mask, last] + distance[last][to]
                dp[key] = min(dp.get(key, INFINITY), value)
    return min(
        dp[FULL, last] + distance[last][END] for last in range(1, END) if last != FORBIDDEN_LAST
    )


def check(distance, data):
    try:
        values = list(map(int, data.split()))
    except ValueError:
        return False
    if len(values) != POINTS + 1:
        return False
    cost, *path = values
    route = [point - 1 for point in path]
    if sorted(route) != list(range(POINTS)):
        return False
    if route[0] != START or route[-1] != END or route[-2] == FORBIDDEN_LAST:
        return False
    actual = sum(distance[a][b] for a, b in zip(route, route[1:]))
    return cost == actual == optimum(distance)


if __name__ == "__main__":
    input_path, _, output_path = map(Path, sys.argv[1:])
    values = list(map(int, input_path.read_text().split()))
    distance = [values[i : i + POINTS] for i in range(0, POINTS * POINTS, POINTS)]
    valid = check(distance, output_path.read_bytes())
    print("OK" if valid else "invalid route, distance or optimum")
    sys.exit(0 if valid else 1)
