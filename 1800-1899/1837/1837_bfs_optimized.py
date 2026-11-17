import sys

CHAMPION = "Isenbaev"
TEAM = 3


def main():
    tokens = sys.stdin.buffer.read().decode().split()
    teams = int(tokens[0])
    members = tokens[1:]
    mates = {}
    for t in range(teams):
        team = members[TEAM * t : TEAM * (t + 1)]
        for name in team:
            mates.setdefault(name, []).extend(team)
    # breadth-first search from the champion over shared teams
    number = {}
    if CHAMPION in mates:
        number[CHAMPION] = 0
        queue = [CHAMPION]
        for name in queue:
            for mate in mates[name]:
                if mate not in number:
                    number[mate] = number[name] + 1
                    queue.append(mate)
    print("\n".join(f"{name} {number.get(name, 'undefined')}" for name in sorted(mates)))


main()
