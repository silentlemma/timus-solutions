import sys

MEDALS = ("gold", "silver", "bronze")
PER_MEDAL = 4
PRIZE = 5


def main():
    stream = sys.stdin
    # each name and forecast occupies its own line; retain only the medallists.
    medal = {stream.readline().strip(): kind for kind in MEDALS for _ in range(PER_MEDAL)}
    best, winners = -1, 0
    for _ in range(int(stream.readline())):
        right = 0
        for _ in range(int(stream.readline())):
            team, _, kind = stream.readline().split()
            right += medal.get(team) == kind
        if right > best:
            best, winners = right, 1
        elif right == best:
            winners += 1
    print(PRIZE * winners)


main()
