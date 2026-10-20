import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, k = data[0], data[1]
    s = data[2:2 + n]
    # Every sponsor needs its own problems, and no problem holds more than k.
    m = max(max(s), -(-sum(s) // k))
    # Write the sponsors one after another and deal the copies round robin:
    # a sponsor's copies are consecutive and at most m, so they land in
    # different problems, and every problem gets at most ceil(total / m) <= k.
    problems = [[] for _ in range(m)]
    position = 0
    for sponsor, wanted in enumerate(s, 1):
        for _ in range(wanted):
            problems[position % m].append(sponsor)
            position += 1
    out = [str(m)]
    out += [" ".join(map(str, [len(p)] + p)) for p in problems]
    print("\n".join(out))


main()
