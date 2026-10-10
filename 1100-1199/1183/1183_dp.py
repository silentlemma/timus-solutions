import sys

PAIR = {"(": ")", "[": "]"}
OPEN = {")": "(", "]": "["}


def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    # add[i][j]: fewest brackets to add so that s[i:j] becomes regular; how
    # it is best done: None pads a lone bracket, -1 wraps a pair, k splits
    add = [[0] * (n + 1) for _ in range(n + 1)]
    how = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if length == 1:
                add[i][j], how[i][j] = 1, None
                continue
            best, way = add[i][i + 1] + add[i + 1][j], i + 1
            if PAIR.get(s[i]) == s[j - 1] and add[i + 1][j - 1] < best:
                best, way = add[i + 1][j - 1], -1
            for k in range(i + 2, j):
                if add[i][k] + add[k][j] < best:
                    best, way = add[i][k] + add[k][j], k
            add[i][j], how[i][j] = best, way
    out = []
    # rebuild with an explicit stack: a lone bracket gets its partner
    todo = [(0, n)]
    while todo:
        item = todo.pop()
        if isinstance(item, str):
            out.append(item)
            continue
        i, j = item
        if i == j:
            continue
        way = how[i][j]
        if way is None:
            c = s[i]
            out.append(c + PAIR[c] if c in PAIR else OPEN[c] + c)
        elif way == -1:
            todo += [s[j - 1], (i + 1, j - 1)]
            out.append(s[i])
        else:
            todo += [(way, j), (i, way)]
    print("".join(out))


main()
