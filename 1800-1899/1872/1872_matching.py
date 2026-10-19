import sys
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    area = data[1:n + 1]
    low, high = data[n + 1::2], data[n + 2::2]
    order = sorted(range(n), key=area.__getitem__)
    sizes = [area[k] for k in order]
    # rooms from the smallest up, each to the waiting team whose largest
    # area is the smallest
    by_low = sorted(range(n), key=low.__getitem__)
    waiting, at, team = [], 0, [0] * n
    for place, size in enumerate(sizes):
        while at < n and low[by_low[at]] <= size:
            heappush(waiting, (high[by_low[at]], by_low[at]))
            at += 1
        if not waiting or waiting[0][0] < size:
            print("Let's search for another office.")
            return
        team[place] = heappop(waiting)[1]
    # the team in room place takes rooms first[place] .. last[place] in sorted
    # order; another seating exists exactly when two teams could swap rooms
    first = [bisect_left(sizes, low[t]) for t in team]
    last = [bisect_right(sizes, high[t]) - 1 for t in team]
    for q in range(1, n):
        if first[q] < q and max(last[first[q]:q]) >= q:
            print("Ask Shiftman for help.")
            return
    room = [0] * n
    for place, t in enumerate(team):
        room[t] = order[place] + 1
    print("Perfect!")
    print(*room)


main()
