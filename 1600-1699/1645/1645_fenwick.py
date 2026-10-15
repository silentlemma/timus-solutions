import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    place = [0] * (n + 1)  # place[s]: finishing position of skier s
    for p in range(1, n + 1):
        place[int(data[p])] = p
    tree = [0] * (n + 1)  # finishing positions of the skiers who started before
    out = []
    for skier in range(1, n + 1):
        p = place[skier]
        earlier = 0  # started before and finished before: undecided
        i = p - 1
        while i:
            earlier += tree[i]
            i &= i - 1
        # started later yet finished before: surely faster
        faster = p - 1 - earlier
        # started before yet finished later: surely slower, the rest undecided
        out.append("%d %d" % (faster + 1, (n - skier) + earlier + 1))
        while p <= n:
            tree[p] += 1
            p += p & -p
    print("\n".join(out))


main()
