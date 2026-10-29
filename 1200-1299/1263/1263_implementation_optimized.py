import sys

PERCENT = 100.0


def main():
    # the votes are read line by line instead of splitting the whole input
    fields = (int(token) for line in sys.stdin.buffer for token in line.split())
    n, m = next(fields), next(fields)
    votes = [0] * (n + 1)
    for _ in range(m):
        votes[next(fields)] += 1
    # candidates with the same count share one formatted line
    percentages = {}
    write = sys.stdout.write
    for candidate in range(1, n + 1):
        count = votes[candidate]
        if count not in percentages:
            percentages[count] = "%.2f%%\n" % (PERCENT * count / m)
        write(percentages[count])


main()
