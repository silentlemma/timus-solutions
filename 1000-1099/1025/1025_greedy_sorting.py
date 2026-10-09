import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    k, size = data[0], sorted(data[1 : 1 + data[0]])
    # win a majority of the groups, choosing the smallest ones; a group of s
    # voters needs s // 2 + 1 supporters
    print(sum(s // 2 + 1 for s in size[: k // 2 + 1]))


main()
