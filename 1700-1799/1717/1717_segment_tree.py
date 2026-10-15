import sys

NEG = -(1 << 62)
FIELDS = 3  # a, f and s of a team


def best_range(sums, counts):
    # the range of f values with the largest total holding at least two
    # teams: for each right end the best left end has the least prefix sum
    # among those leaving at least two teams inside
    prefix, inside = [0], [0]
    for s, c in zip(sums, counts):
        prefix.append(prefix[-1] + s)
        inside.append(inside[-1] + c)
    best, where = NEG, (0, 0)
    low, low_at, t = NEG, 0, 0
    for r in range(1, len(prefix)):
        while t < r and inside[t] <= inside[r] - 2:
            if low == NEG or prefix[t] < low:
                low, low_at = prefix[t], t
            t += 1
        if low != NEG and prefix[r] - low > best:
            best, where = prefix[r] - low, (low_at, r - 1)
    return where


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    teams = [tuple(int(w) for w in data[1 + FIELDS * i:1 + FIELDS * (i + 1)]) for i in range(n)]
    ages = sorted({a for a, _, _ in teams})
    fs = sorted({f for _, f, _ in teams})
    age_at = {a: i for i, a in enumerate(ages)}
    f_at = {f: i for i, f in enumerate(fs)}
    by_age = [[] for _ in ages]
    for a, f, s in teams:
        by_age[age_at[a]].append((f_at[f], s))
    size = 1
    while size < len(fs):
        size *= 2
    width = 2 * size
    # every node of the tree over f keeps its total, its count of teams
    # (capped at 2), its best prefix and suffix with exactly 0, 1 or 2+
    # teams, and its best range with at least two teams
    answer, answer_ages = NEG, (0, 0)
    for left in range(len(ages)):
        total = [0] * width
        kind = [0] * width
        p0, p1, p2 = [0] * width, [NEG] * width, [NEG] * width
        s0, s1, s2 = [0] * width, [NEG] * width, [NEG] * width
        best = [NEG] * width
        for right in range(left, len(ages)):
            for fi, s in by_age[right]:
                v = size + fi
                c = min(kind[v] + 1, 2)
                t = total[v] + s
                total[v], kind[v] = t, c
                p0[v] = p1[v] = p2[v] = NEG
                if c == 1:
                    p1[v] = t
                else:
                    p2[v] = t
                s0[v], s1[v], s2[v] = p0[v], p1[v], p2[v]
                best[v] = t if c == 2 else NEG
                v >>= 1
                while v:
                    a = 2 * v
                    b = a + 1
                    ta, tb, ka, kb = total[a], total[b], kind[a], kind[b]
                    total[v] = ta + tb
                    kind[v] = ka + kb if ka + kb < 2 else 2
                    # prefixes: inside the left child, or all of it and more
                    q0, q1, q2 = p0[a], p1[a], p2[a]
                    for j, x in ((0, p0[b]), (1, p1[b]), (2, p2[b])):
                        if x != NEG:
                            x += ta
                            k = ka + j
                            if k == 0:
                                q0 = x if x > q0 else q0
                            elif k == 1:
                                q1 = x if x > q1 else q1
                            else:
                                q2 = x if x > q2 else q2
                    p0[v], p1[v], p2[v] = q0, q1, q2
                    # suffixes: inside the right child, or all of it and more
                    r0, r1, r2 = s0[b], s1[b], s2[b]
                    for j, x in ((0, s0[a]), (1, s1[a]), (2, s2[a])):
                        if x != NEG:
                            x += tb
                            k = kb + j
                            if k == 0:
                                r0 = x if x > r0 else r0
                            elif k == 1:
                                r1 = x if x > r1 else r1
                            else:
                                r2 = x if x > r2 else r2
                    s0[v], s1[v], s2[v] = r0, r1, r2
                    # ranges: inside a child, or across with two or more teams
                    top = best[a] if best[a] > best[b] else best[b]
                    a0, a1, a2 = s0[a], s1[a], s2[a]
                    b0, b1, b2 = p0[b], p1[b], p2[b]
                    for x, y in ((a0, b2), (a1, b1), (a1, b2), (a2, b0), (a2, b1), (a2, b2)):
                        if x != NEG and y != NEG and x + y > top:
                            top = x + y
                    best[v] = top
                    v >>= 1
            if best[1] > answer:
                answer, answer_ages = best[1], (left, right)
    left, right = answer_ages
    sums, counts = [0] * len(fs), [0] * len(fs)
    for r in range(left, right + 1):
        for fi, s in by_age[r]:
            sums[fi] += s
            counts[fi] += 1
    lo, hi = best_range(sums, counts)
    print(ages[left], ages[right])
    print(fs[lo], fs[hi])


main()
