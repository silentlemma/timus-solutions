import sys

PERCENT = 100.0


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    votes = [0] * (n + 1)
    for t in data[2 : 2 + m]:
        votes[int(t)] += 1
    sys.stdout.write("".join("%.2f%%\n" % (PERCENT * v / m) for v in votes[1:]))


main()
