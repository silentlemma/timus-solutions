import sys


def reliable_teams(values):
    ordered = sorted((value, index + 1) for index, value in enumerate(values))
    teams = []
    count = len(ordered)
    for size in range(1, count + 1):
        if ordered[size - 1][0] <= size and (
            size == count or ordered[size][0] > size + 1
        ):
            teams.append([index for _, index in ordered[:size]])
    return teams


def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    teams = reliable_teams(tokens[1 : tokens[0] + 1])
    lines = [str(len(teams))]
    lines.extend(" ".join(map(str, [len(team), *team])) for team in teams)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
