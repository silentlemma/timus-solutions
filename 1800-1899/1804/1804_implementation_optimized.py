import sys


MOST = 30
VENUE_FIELD = 3
SCORED_FIELD = 6
CONCEDED_FIELD = 10


def main():
    read = sys.stdin.buffer.readline
    output = []
    for _ in range(int(read())):
        words = read().split()
        home = words[VENUE_FIELD] == b"home"
        x, y = int(words[SCORED_FIELD]), int(words[CONCEDED_FIELD])
        lowest = highest = -1
        for goals in range(MOST + 1):
            ours = (x + goals, goals if home else x)
            # Zero opposing goals maximize our chance; MOST minimize it.
            if lowest < 0 and ours >= (y, y if home else 0):
                lowest = goals
            if ours <= (y + MOST, y if home else MOST):
                highest = goals
        output.append(f"{lowest} {highest}")
    sys.stdout.write("\n".join(output) + "\n")


main()
