import sys


def main():
    tok = iter(map(int, sys.stdin.buffer.read().split()))
    first = [(next(tok), next(tok), next(tok)) for _ in range(next(tok))]
    second = [(next(tok), next(tok), next(tok)) for _ in range(next(tok))]
    out = []
    j = 0
    for a, b, y in first:
        cur = a
        # walk through [a, b) and keep what no interval of the second covers
        while cur < b:
            while j < len(second) and second[j][1] <= cur:
                j += 1
            if j < len(second) and second[j][0] <= cur:
                cur = second[j][1]
                continue
            end = min(b, second[j][0]) if j < len(second) else b
            out.append("%d %d %d" % (cur, end, y))
            cur = end
    print(" ".join([str(len(out))] + out))


main()
