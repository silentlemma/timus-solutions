def start(x):
    # numbers below 10^(d-1) take (d-1)·10^(d-1) - R(d-1) digits, where R(t)
    # is the repunit of t ones; adding d digits per number from 10^(d-1) on
    # leaves d·x + 1 - R(d) for the position of the first digit of x
    d = len(str(x))
    return d * x + 1 - int("1" * d)


def fits(a, s, x):
    # whether the number x can begin at position s of a, with its neighbours
    # filling the rest of a on both sides
    n, xs = len(a), str(x)
    if a[s : s + len(xs)] != xs[: n - s]:
        return False
    pos, cur = s + len(xs), x
    while pos < n:
        cur += 1
        cs = str(cur)
        if a[pos : pos + len(cs)] != cs[: n - pos]:
            return False
        pos += len(cs)
    pos, cur = s, x
    while pos > 0:
        cur -= 1
        if cur <= 0:
            return False
        cs = str(cur)
        if a[max(0, pos - len(cs)) : pos] != cs[max(0, len(cs) - pos) :]:
            return False
        pos -= len(cs)
    return True


def main():
    a = input().strip()
    n = len(a)
    # a inside one number, right after its first digit
    best = start(int("1" + a)) + 1
    # some number lies in a completely
    for s in range(n):
        if a[s] != "0":
            for e in range(s + 1, n + 1):
                x = int(a[s:e])
                if fits(a, s, x):
                    best = min(best, start(x) - s)
    # a is the end of y - 1 followed by the beginning of y; the last i digits
    # of y are those of y - 1 plus one, and they may overlap the known
    # beginning by j digits
    for i in range(1, n):
        if a[i] == "0":
            continue
        tail = str((int(a[:i]) + 1) % 10**i).zfill(i)
        for j in range(min(n - i, i) + 1):
            if a[n - j :] == tail[:j]:
                y = int(a[i:] + tail[j:])
                if fits(a, i, y):
                    best = min(best, start(y) - i)
    print(best)


main()
