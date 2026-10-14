import sys


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    groups = [int(x) for x in data[2 : 2 + k]]
    line = data[2 + k] if len(data) > 2 + k else ""
    dots = [0] * (n + 1)  # dots[i]: known empty cells among the first i
    for i, ch in enumerate(line):
        dots[i + 1] = dots[i] + (ch == ".")

    def fits(s, length):
        """Whether a group can cover the cells s ... s + length - 1."""
        return 0 <= s and s + length <= n and dots[s + length] == dots[s]

    # pre[i][j]: the first i cells can hold the first j groups
    pre = [[False] * (k + 1) for _ in range(n + 1)]
    pre[0][0] = True
    for i in range(1, n + 1):
        for j in range(k + 1):
            ok = line[i - 1] != "X" and pre[i - 1][j]
            if not ok and j > 0 and fits(i - groups[j - 1], groups[j - 1]):
                s = i - groups[j - 1]
                ok = j == 1 if s == 0 else line[s - 1] != "X" and pre[s - 1][j - 1]
            pre[i][j] = ok
    if not pre[n][k]:
        print("Impossible")
        return
    # suf[i][j]: the cells from i on can hold the groups from j on
    suf = [[False] * (k + 1) for _ in range(n + 2)]
    suf[n][k] = True
    for i in range(n - 1, -1, -1):
        for j in range(k, -1, -1):
            ok = line[i] != "X" and suf[i + 1][j]
            if not ok and j < k and fits(i, groups[j]):
                end = i + groups[j]
                ok = j + 1 == k if end == n else line[end] != "X" and suf[end + 1][j + 1]
            suf[i][j] = ok

    white = [
        line[c] != "X" and any(pre[c][j] and suf[c + 1][j] for j in range(k + 1)) for c in range(n)
    ]
    cover = [0] * (n + 1)  # difference array of the cells some group can cover
    for j, length in enumerate(groups):
        for s in range(n - length + 1):
            if not fits(s, length):
                continue
            end = s + length
            left = j == 0 if s == 0 else line[s - 1] != "X" and pre[s - 1][j]
            right = j + 1 == k if end == n else line[end] != "X" and suf[end + 1][j + 1]
            if left and right:
                cover[s] += 1
                cover[end] -= 1
    out, run = [], 0
    for c in range(n):
        run += cover[c]
        out.append("?" if white[c] and run else ("." if white[c] else "X"))
    print("".join(out))


main()
