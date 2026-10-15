import sys

COPIES = 4  # the text repeated so that every comparison below stays inside it


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    s = data[1]
    n = len(s)
    t = s * COPIES
    # a substring is counted at its leftmost start j in the window [a, a + k):
    # its lengths up to a + k - j minus the longest common prefix of j with an
    # earlier start of the window, best[j]; going down over a adds start a
    top = n + 2 * k
    common = [0] * k  # common[d] = lcp of positions a and a + d
    best = [0] * (top + k)
    answers = [0] * n
    for a in range(top, -1, -1):
        ca = t[a]
        for d in range(1, k):
            j = a + d
            if t[j] == ca:
                length = common[d] + 1
                common[d] = length
                if length > best[j]:
                    best[j] = length
            else:
                common[d] = 0
        if a < n:
            end = a + k
            total = 0
            for j in range(a, end):
                fresh = end - j - best[j]
                if fresh > 0:
                    total += fresh
            answers[a] = total
    print(" ".join(map(str, answers)))


main()
