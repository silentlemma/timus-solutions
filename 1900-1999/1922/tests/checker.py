"""Validate all reliable nonempty teams, ignoring team and member order."""

from pathlib import Path
import sys


def expected_teams(values):
    count = len(values)
    frequency = [0] * (max(max(values), count + 1) + 1)
    for value in values:
        frequency[value] += 1
    eligible = 0
    teams = set()
    for size in range(1, count + 1):
        eligible += frequency[size]
        if eligible == size and frequency[size + 1] == 0:
            teams.add(
                frozenset(
                    index + 1 for index, value in enumerate(values) if value <= size
                )
            )
    return teams


def check(values, output):
    try:
        tokens = list(map(int, output.split()))
    except ValueError:
        return False, "noninteger output"
    count = len(values)
    if not tokens or not 0 <= tokens[0] <= count:
        return False, "invalid team count"
    position = 1
    emitted = set()
    for _ in range(tokens[0]):
        if position >= len(tokens):
            return False, "missing team size"
        size = tokens[position]
        position += 1
        if not 1 <= size <= count or position + size > len(tokens):
            return False, "invalid nonempty team size"
        members = tokens[position : position + size]
        position += size
        if any(not 1 <= member <= count for member in members):
            return False, "member index outside input"
        team = frozenset(members)
        if len(team) != size:
            return False, "duplicate member"
        if team in emitted:
            return False, "duplicate team"
        if any(values[member - 1] > size for member in team):
            return False, "team is not effective"
        if any(
            index + 1 not in team and value <= size + 1
            for index, value in enumerate(values)
        ):
            return False, "one outsider can be added effectively"
        emitted.add(team)
    if position != len(tokens):
        return False, "extra output"
    return emitted == expected_teams(
        values
    ), "the complete set of reliable teams is required"


if __name__ == "__main__":
    data = list(map(int, Path(sys.argv[1]).read_text().split()))
    accepted, reason = check(data[1 : data[0] + 1], Path(sys.argv[3]).read_text())
    print(reason)
    sys.exit(0 if accepted else 1)
