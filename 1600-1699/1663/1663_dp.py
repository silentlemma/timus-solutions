import sys

TOLL = 1000


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    people = [int(w) for w in data[1:1 + n]]
    if n == 2:
        print(1, 2)
        return
    order = sorted(range(n), key=lambda i: people[i])
    p = [people[i] for i in order]
    q = [TOLL // x for x in p]
    # towns sorted by size: the best tour climbs to the last town on one path
    # and comes back on the other; up[j] costs a climb ending at the newest
    # town and a return ending at town j, down[j] the other way round
    up, down = [q[0] * p[1]], [q[1] * p[0]]
    shift_up = shift_down = 0
    from_down, from_up = [0, 0], [0, 0]
    for m in range(1, n - 2):
        nxt = m + 1
        best_up = min(range(m), key=lambda j: down[j] + q[j] * p[nxt])
        best_down = min(range(m), key=lambda j: up[j] + q[nxt] * p[j])
        new_up = down[best_up] + shift_down + q[best_up] * p[nxt]
        new_down = up[best_down] + shift_up + q[nxt] * p[best_down]
        shift_up += q[m] * p[nxt]
        shift_down += q[nxt] * p[m]
        up.append(new_up - shift_up)
        down.append(new_down - shift_down)
        from_down.append(best_up)
        from_up.append(best_down)
    last, m = n - 1, n - 2
    close_up = [up[j] + shift_up + q[m] * p[last] + q[last] * p[j] for j in range(m)]
    close_down = [down[j] + shift_down + q[j] * p[last] + q[last] * p[m] for j in range(m)]
    j_up = min(range(m), key=close_up.__getitem__)
    j_down = min(range(m), key=close_down.__getitem__)
    climbing = close_up[j_up] <= close_down[j_down]
    j = j_up if climbing else j_down
    # walk back: town m is on the climbing path or not, the other path ends at j
    on_up = [False] * n
    while m >= 1:
        on_up[m] = climbing
        if j == m - 1:
            j = from_down[m] if climbing else from_up[m]
            climbing = not climbing
        m -= 1
    tour = [0] + [k for k in range(1, n - 1) if on_up[k]] + [n - 1]
    tour += [k for k in range(n - 2, 0, -1) if not on_up[k]]
    tour = [order[k] for k in tour]
    start = tour.index(0)
    print(" ".join(str(t + 1) for t in tour[start:] + tour[:start]))


main()
