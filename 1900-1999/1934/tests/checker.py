"""Check shortest length, near-optimal path risk and reported probability independently of logs."""

from array import array
from fractions import Fraction
from pathlib import Path
import re
import sys

PERCENT_SCALE = 100
PROBABILITY_SCALE = 10**24
MAX_ERROR = Fraction(1, 1000000)
REAL_PATTERN = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?")


def shortest_layers(adjacency, start):
    distance = array("i", [-1]) * len(adjacency)
    distance[start] = 0
    order = [start]
    for city in order:
        following = distance[city] + 1
        for edge in adjacency[city]:
            neighbor = edge // PERCENT_SCALE
            if distance[neighbor] < 0:
                distance[neighbor] = following
                order.append(neighbor)
    return distance, order


def check(adjacency, start, target, output):
    tokens = output.split()
    if len(tokens) < 2:
        return False, "missing path length or probability"
    if REAL_PATTERN.fullmatch(tokens[1]) is None:
        return False, "probability is not a finite decimal number"
    try:
        length = int(tokens[0])
        reported = Fraction(tokens[1])
        path = [int(token) - 1 for token in tokens[2:]]
    except (ValueError, ZeroDivisionError):
        return False, "invalid numeric output"
    count = len(adjacency)
    if not 2 <= length <= count or len(path) != length:
        return False, "wrong path length or identifier count"
    if any(not 0 <= city < count for city in path):
        return False, "path identifier out of range"
    if path[0] != start or path[-1] != target:
        return False, "wrong path endpoints"
    if not 0 <= reported <= 1:
        return False, "probability outside zero to one"
    distance, order = shortest_layers(adjacency, start)
    if distance[target] < 0 or length != distance[target] + 1:
        return False, "path does not minimize visited vertices"
    route_survival = PROBABILITY_SCALE
    for index, (city, following) in enumerate(zip(path, path[1:])):
        if distance[city] != index or distance[following] != index + 1:
            return False, "path leaves shortest layers"
        for edge in adjacency[city]:
            neighbor, probability = divmod(edge, PERCENT_SCALE)
            if neighbor == following:
                route_survival = (
                    route_survival * (PERCENT_SCALE - probability) // PERCENT_SCALE
                )
                break
        else:
            return False, "path uses a missing edge"
    best = [-1] * count
    best[start] = PROBABILITY_SCALE
    for city in order:
        if distance[city] >= distance[target]:
            continue
        following_distance = distance[city] + 1
        for edge in adjacency[city]:
            neighbor, probability = divmod(edge, PERCENT_SCALE)
            if distance[neighbor] == following_distance:
                candidate = best[city] * (PERCENT_SCALE - probability) // PERCENT_SCALE
                if candidate > best[neighbor]:
                    best[neighbor] = candidate
    # Each downward rounding loses less than one scale unit per path edge.
    rounding_slack = 2 * count
    tolerance_units = PROBABILITY_SCALE * MAX_ERROR
    if best[target] - route_survival > tolerance_units + rounding_slack:
        return False, "shortest path risk is worse than the permitted optimum error"
    path_risk = Fraction(PROBABILITY_SCALE - route_survival, PROBABILITY_SCALE)
    if abs(reported - path_risk) > MAX_ERROR + Fraction(
        rounding_slack, PROBABILITY_SCALE
    ):
        return False, "reported probability does not describe the path"
    return True, "valid shortest path with near-optimal risk and accurate probability"


def read_input(path):
    values = iter(map(int, Path(path).read_text().split()))
    count, roads = next(values), next(values)
    start, target = next(values) - 1, next(values) - 1
    adjacency = [[] for _ in range(count)]
    for _ in range(roads):
        first, second, probability = next(values) - 1, next(values) - 1, next(values)
        adjacency[first].append(PERCENT_SCALE * second + probability)
        adjacency[second].append(PERCENT_SCALE * first + probability)
    return adjacency, start, target


if __name__ == "__main__":
    graph, source, destination = read_input(sys.argv[1])
    accepted, reason = check(graph, source, destination, Path(sys.argv[3]).read_text())
    print(reason)
    sys.exit(0 if accepted else 1)
