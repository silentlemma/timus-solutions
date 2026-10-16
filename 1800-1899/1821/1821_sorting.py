import sys

# times in tenths of a second; starts are 30 seconds apart
TENTHS_PER_MINUTE = 600
TENTHS_PER_SECOND = 10
GAP = 300


def tenths(text):
    minutes, rest = text.split(":")
    seconds, tenth = rest.split(".")
    return int(minutes) * TENTHS_PER_MINUTE + int(seconds) * TENTHS_PER_SECOND + int(tenth)


def main():
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    runs = []
    for i in range(n):
        name, time = tokens[1 + 2 * i], tokens[2 + 2 * i]
        run = tenths(time)
        runs.append((i * GAP + run, run, name))
    # replay the finishes in order; the board changes on every new best run
    leaders = []
    best = None
    for _, run, name in sorted(runs):
        if best is None or run < best:
            best = run
            leaders.append(name)
    leaders.sort()
    print(len(leaders))
    print("\n".join(leaders))


main()
