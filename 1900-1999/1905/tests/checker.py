"""Validate a flight route by its real closed visit intervals, including waiting."""

from pathlib import Path
import sys


def check(input_text, expected_text, output_text):
    expected = expected_text.split()
    tokens = output_text.split()
    if tokens == ["Impossible"]:
        return None if expected == ["Impossible"] else "a route exists"
    try:
        values = list(map(int, tokens))
    except ValueError:
        return "expected Impossible or integer flight indices"
    if not values or values[0] < 0 or len(values) != values[0] + 1:
        return "the flight count does not match the number of indices"
    source = iter(map(int, input_text.split()))
    next(source)
    count = next(source)
    flights = [tuple(next(source) for _ in range(4)) for _ in range(count)]
    planet, target, now, deadline = (next(source) for _ in range(4))
    if values[0] > count:
        return "a flight cannot be repeated without revisiting its departure event"
    visits = []
    for index in values[1:]:
        if not 1 <= index <= count:
            return "a flight index is out of range"
        departure, arrival, leave, enter = flights[index - 1]
        if departure != planet:
            return "a flight leaves from a different planet"
        if leave < now:
            return "a flight departed before the current arrival"
        visits.append((planet, now, leave))
        planet, now = arrival, enter
    if planet != target or now > deadline:
        return "the final planet or arrival time misses the target event"
    visits.append((planet, now, deadline))
    visits.sort()
    for before, after in zip(visits, visits[1:]):
        if before[0] == after[0] and after[1] <= before[2]:
            return "two visits to the same planet overlap in real time"
    return None


def main():
    input_path, expected_path, output_path = map(Path, sys.argv[1:])
    error = check(
        input_path.read_text(), expected_path.read_text(), output_path.read_text()
    )
    if error is not None:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
