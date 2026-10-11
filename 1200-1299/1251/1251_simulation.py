import heapq
import sys

FORGET = 1001  # a grave untouched for 1000 days can go on the next day
NOTICE = 101  # and only when no neighbour was visited in the last 100


def main():
    words = sys.stdin.read().split()
    n, m = int(words[0]), int(words[1])
    cells = n * m
    # the client in each grave (0 if free), the last burial or visit of that
    # client, the last visit next door and the day the grave may be freed
    owner, touched, near_visit, release = [0] * cells, [0] * cells, [-NOTICE] * cells, [0] * cells
    grave_of = []  # grave of each client, -1 if none
    free = list(range(cells))
    pending = []
    neighbours = []
    for g in range(cells):
        r, c = divmod(g, m)
        neighbours.append(
            [
                nr * m + nc
                for nr in range(r - 1, r + 2)
                for nc in range(c - 1, c + 2)
                if (nr, nc) != (r, c) and 0 <= nr < n and 0 <= nc < m
            ]
        )

    def schedule(g):
        release[g] = max(touched[g] + FORGET, near_visit[g] + NOTICE)
        heapq.heappush(pending, (release[g], g))

    cremated = 0
    k = 2
    while k < len(words):
        day, kind = int(words[k]), words[k + 1]
        k += 2
        # graves free at the start of the day, before its events
        while pending and pending[0][0] <= day:
            when, g = heapq.heappop(pending)
            if owner[g] and release[g] == when:
                grave_of[owner[g] - 1] = -1
                owner[g] = 0
                heapq.heappush(free, g)
        if kind == "d":
            grave_of.append(-1)
            if not free:
                cremated += 1
                continue
            g = heapq.heappop(free)
            owner[g] = len(grave_of)
            grave_of[-1] = g
            touched[g] = day
            schedule(g)
            continue
        g = grave_of[int(words[k]) - 1]
        k += 1
        if g < 0:
            continue
        touched[g] = day
        schedule(g)
        for h in neighbours[g]:
            near_visit[h] = day
            if owner[h]:
                schedule(h)
    print(cremated)


main()
