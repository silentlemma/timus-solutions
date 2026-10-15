import sys


def main():
    n = int(sys.stdin.readline())
    # every two flags need a common color, and a color on at most two flags
    # serves one pair only, so k(k - 1) / 2 <= n; one color per pair is enough
    k = 1
    while (k + 1) * k // 2 <= n:
        k += 1
    flags = [[] for _ in range(k)]
    color = 0
    for a in range(k):
        for b in range(a + 1, k):
            color += 1
            flags[a].append(color)
            flags[b].append(color)
    out = [str(k)]
    for flag in flags:
        out.append(" ".join(map(str, [len(flag)] + flag)))
    print("\n".join(out))


main()
