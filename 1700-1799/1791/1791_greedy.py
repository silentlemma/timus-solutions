import sys


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    ready, last = [], []
    for _ in range(2):
        count = int(data[pos])
        times = list(map(int, data[pos + 1:pos + 1 + 2 * count]))
        pos += 1 + 2 * count
        r = times[0::2]
        d = [t + p - 1 for t, p in zip(r, times[1::2])]
        # a bus must enter before the next one on its side
        for i in range(count - 2, -1, -1):
            if d[i] > d[i + 1] - 1:
                d[i] = d[i + 1] - 1
        ready.append(r)
        last.append(d)
    sizes = [len(ready[0]), len(ready[1])]
    head = [0, 0]
    now = 0
    while head[0] < sizes[0] or head[1] < sizes[1]:
        # among the waiting front buses, the one with the earlier last minute
        pick = -1
        soonest = -1
        for s in (0, 1):
            h = head[s]
            if h == sizes[s]:
                continue
            if soonest < 0 or ready[s][h] < soonest:
                soonest = ready[s][h]
            if ready[s][h] <= now and (pick < 0 or last[s][h] < last[pick][head[pick]]):
                pick = s
        if pick < 0:
            now = soonest
            continue
        if now > last[pick][head[pick]]:
            print("NO")
            return
        head[pick] += 1
        now += 1
    print("YES")


main()
