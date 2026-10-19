from itertools import combinations, permutations, product
from math import gcd
import sys


TEAM_COUNT = 4
WIN_POINTS = 3


def simplify(rows):
    unique = {}
    for coefficients, bound in rows:
        divisor = 0
        for value in coefficients:
            divisor = gcd(divisor, value)
        if not divisor:
            if bound < 0:
                return None
            continue
        coefficients = tuple(value // divisor for value in coefficients)
        bound //= divisor
        if coefficients not in unique or bound < unique[coefficients]:
            unique[coefficients] = bound
    return list(unique.items())


def integer_feasible(rows):
    rows = simplify(rows)
    while rows:
        dimension = len(rows[0][0])
        choices = []
        for column in range(dimension):
            positive = negative = 0
            unit_upper = unit_lower = True
            for coefficients, _ in rows:
                value = coefficients[column]
                if value > 0:
                    positive += 1
                    unit_upper = unit_upper and value == 1
                elif value < 0:
                    negative += 1
                    unit_lower = unit_lower and value == -1
            if unit_upper or unit_lower:
                choices.append((positive * negative, column))
        _, column = min(choices)
        lower = []
        upper = []
        projected = []
        for coefficients, bound in rows:
            value = coefficients[column]
            if value < 0:
                lower.append((coefficients, bound))
            elif value > 0:
                upper.append((coefficients, bound))
            else:
                projected.append(
                    (coefficients[:column] + coefficients[column + 1 :], bound)
                )
        for a, b in lower:
            for c, d in upper:
                coefficients = tuple(
                    c[column] * a[j] - a[column] * c[j]
                    for j in range(dimension)
                    if j != column
                )
                projected.append((coefficients, c[column] * b - a[column] * d))
        rows = simplify(projected)
    return rows is not None


def possible_orders(matches):
    pairs = list(combinations(range(TEAM_COUNT), 2))
    played = set()
    initial_points = [0] * TEAM_COUNT
    initial_difference = [0] * TEAM_COUNT
    for a, b, c, d in matches:
        played.add((a, b))
        initial_difference[a] += c - d
        initial_difference[b] += d - c
        if c == d:
            initial_points[a] += 1
            initial_points[b] += 1
        else:
            initial_points[a if c > d else b] += WIN_POINTS
    remaining = [pair for pair in pairs if pair not in played]
    orders = list(permutations(range(TEAM_COUNT)))
    found = set()
    for outcomes in product(range(WIN_POINTS), repeat=len(remaining)):
        points = initial_points[:]
        difference = initial_difference[:]
        edges = []
        for (a, b), outcome in zip(remaining, outcomes):
            if outcome == 0:
                points[a] += 1
                points[b] += 1
            else:
                winner, loser = (a, b) if outcome == 1 else (b, a)
                points[winner] += WIN_POINTS
                difference[winner] += 1
                difference[loser] -= 1
                edges.append((winner, loser))
        for order in orders:
            if order in found:
                continue
            if any(points[a] < points[b] for a, b in zip(order, order[1:])):
                continue
            rows = []
            for column in range(len(edges)):
                rows.append((tuple(-int(j == column) for j in range(len(edges))), 0))
            for a, b in zip(order, order[1:]):
                if points[a] == points[b]:
                    coefficients = tuple(
                        int(winner == b)
                        - int(loser == b)
                        - int(winner == a)
                        + int(loser == a)
                        for winner, loser in edges
                    )
                    rows.append((coefficients, difference[a] - difference[b]))
            if integer_feasible(rows):
                found.add(order)
        if len(found) == len(orders):
            break
    return sorted(found)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    matches = []
    for index in range(data[0]):
        at = 1 + TEAM_COUNT * index
        a, b, c, d = data[at : at + TEAM_COUNT]
        matches.append((a - 1, b - 1, c, d))
    orders = possible_orders(matches)
    print(len(orders))
    for order in orders:
        print(*(team + 1 for team in order))


if __name__ == "__main__":
    main()
