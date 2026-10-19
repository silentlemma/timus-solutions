"""Check team membership and every game event without trusting the stored answer."""

import sys

TEAM_SIZE = 4
HEALTHY = 3
WOUNDED = 2
DYING = 1


class Bad(Exception):
    pass


def read_log(source):
    lines = open(source, encoding="utf-8").read().splitlines()
    count = int(lines[0])
    names = lines[1 : count + 1]
    events = [line.split() for line in lines[count + 2 :]]
    return names, events


def simulate(names, events, teams=None):
    health = dict.fromkeys(names, HEALTHY)
    edges = {name: [] for name in names}
    for event in events:
        actor, action = event[:2]
        if health[actor] < WOUNDED:
            return False, edges
        if action == "USES":
            health[actor] = HEALTHY
            continue
        target = event[2]
        if action == "HIT":
            damage = 1 if event[-1] == "BODY" else 2
            health[target] = max(0, health[target] - damage)
        else:
            if health[target] != DYING:
                return False, edges
            if teams is not None and teams[actor] != teams[target]:
                return False, edges
            health[target] = WOUNDED
            edges[actor].append(target)
            edges[target].append(actor)
    return True, edges


def feasible(names, events):
    valid, edges = simulate(names, events)
    if not valid:
        return False
    seen = set()
    counts = [0] * (TEAM_SIZE + 1)
    for name in names:
        if name in seen:
            continue
        seen.add(name)
        stack = [name]
        size = 0
        while stack:
            vertex = stack.pop()
            size += 1
            for neighbor in edges[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        if size > TEAM_SIZE:
            return False
        counts[size] += 1
    singles = counts[1] - counts[TEAM_SIZE - 1]
    if singles < 0:
        return False
    # Triples need singles; an unpaired double needs two more singles.
    return counts[2] % 2 == 0 or singles >= 2


def check(source, expected, output):
    names, events = read_log(source)
    lines = open(output, encoding="utf-8").read().splitlines()
    if not lines or lines[0].split() not in (["FAKE"], ["CORRECT"]):
        raise Bad("expected FAKE or CORRECT on the first line")
    if lines[0].split() == ["FAKE"]:
        if any(line.split() for line in lines[1:]):
            raise Bad("unexpected text after FAKE")
        if feasible(names, events):
            raise Bad("the log admits a valid team partition")
        return
    rows = lines[1:]
    while rows and not rows[-1].split():
        rows.pop()
    if len(rows) != len(names) // TEAM_SIZE:
        raise Bad("expected exactly one row for each team")
    teams = {}
    known = set(names)
    for index, row in enumerate(rows):
        members = row.split()
        if len(members) != TEAM_SIZE:
            raise Bad("each team must contain exactly four names")
        for name in members:
            if name not in known or name in teams:
                raise Bad("unknown or repeated player name")
            teams[name] = index
    if set(teams) != known:
        raise Bad("every player must appear exactly once")
    valid, _ = simulate(names, events, teams)
    if not valid:
        raise Bad("the log violates a health or team rule")


def main():
    try:
        check(*sys.argv[1:TEAM_SIZE])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
