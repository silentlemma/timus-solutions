import sys

INF = float("inf")


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    gaps = data[1:n]
    start, period, first_up, first_down = (x for x in data[n:])
    start -= 1
    if n == 1:
        print(0)
        return
    pos = [0] * n
    for i in range(1, n):
        pos[i] = pos[i - 1] + gaps[i - 1]
    # trains run forever: towards N they pass station i at first_up + pos[i]
    # plus multiples of the period, towards 1 at first_down + pos[N] - pos[i]
    phase = [
        [(first_up + pos[i]) % period for i in range(n)],
        [(first_down + pos[-1] - pos[i]) % period for i in range(n)],
    ]
    # rides from j in each direction: (phase there, stations that way)
    rides = [
        [(phase[0][j], ((1 << n) - 1) >> (j + 1) << (j + 1)), (phase[1][j], (1 << j) - 1)]
        for j in range(n)
    ]
    full = (1 << n) - 1
    best = INF
    for d0 in range(2):
        t0 = phase[d0][start]
        # arrive[mask * n + j]: earliest time standing at j with mask inspected
        arrive = [INF] * ((full + 1) * n)
        rest = rides[start][d0][1]
        while rest:
            k = (rest & -rest).bit_length() - 1
            rest &= rest - 1
            arrive[(1 << start | 1 << k) * n + k] = t0 + abs(pos[k] - pos[start])
        for mask in range(full):
            if not mask >> start & 1:
                continue
            base = mask * n
            for j in range(n):
                t = arrive[base + j]
                if t == INF:
                    continue
                pj = pos[j]
                for ph, way in rides[j]:
                    rest = way & ~mask
                    if not rest:
                        continue
                    dep = t + 1 + (ph - t - 1) % period
                    while rest:
                        bit = rest & -rest
                        rest ^= bit
                        k = bit.bit_length() - 1
                        a = dep + abs(pos[k] - pj)
                        at = (mask | bit) * n + k
                        if a < arrive[at]:
                            arrive[at] = a
        # with everything inspected, ride straight back to the start
        for j in range(n):
            t = arrive[full * n + j]
            if t != INF and j != start:
                ph = phase[0 if start > j else 1][j]
                dep = t + 1 + (ph - t - 1) % period
                best = min(best, dep + abs(pos[start] - pos[j]) - t0)
    print(best)


main()
