import sys

STEP = 10  # every tenth person is fined
INF = 1 << 30


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    good = data[2] if n else ""
    # cost[i][j] holds the least fines once i conductors and j friends stand
    # in line, and the next person then stands at place i + j + 1
    cost = [[INF] * (k + 1) for _ in range(n + 1)]
    cost[0][0] = 0
    for i in range(n + 1):
        row = cost[i]
        for j in range(k + 1):
            here = row[j]
            if here == INF:
                continue
            fined = (i + j + 1) % STEP == 0
            if j < k and here + fined < row[j + 1]:
                row[j + 1] = here + fined  # a friend steps in
            if i < n:
                nxt = here + (fined and good[i] == "1")
                if nxt < cost[i + 1][j]:
                    cost[i + 1][j] = nxt
    best = min(cost[n])
    j = cost[n].index(best)
    # walk back: a friend was added wherever the cost came from the left
    places = []
    i = n
    while i > 0 or j > 0:
        fined = (i + j) % STEP == 0
        if i > 0 and cost[i - 1][j] + (fined and good[i - 1] == "1") == cost[i][j]:
            i -= 1
        else:
            places.append(i + j)
            j -= 1
    places.reverse()
    print(best)
    print(" ".join(map(str, [len(places)] + places)))


main()
