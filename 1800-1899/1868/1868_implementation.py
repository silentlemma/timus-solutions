import sys

MEDALS = ("gold", "silver", "bronze")
PER_MEDAL = 4
PRIZE = 5


def main():
    words = iter(sys.stdin.read().split())
    medal = {}
    for kind in MEDALS:
        for _ in range(PER_MEDAL):
            medal[next(words)] = kind
    scores = []
    for _ in range(int(next(words))):
        right = 0
        for _ in range(int(next(words))):
            team, _, kind = next(words), next(words), next(words)
            right += medal.get(team) == kind
        scores.append(right)
    print(PRIZE * scores.count(max(scores)))


main()
