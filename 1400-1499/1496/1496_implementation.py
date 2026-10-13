import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # a team that submitted more than once is the spammer; dictionaries keep
    # the first-seen order, which is as good as any
    count = {}
    for team in data[1 : n + 1]:
        count[team] = count.get(team, 0) + 1
    print("\n".join(team for team, c in count.items() if c > 1))


main()
