import sys


def main():
    text, name = sys.stdin.read().split()[:2]
    n, m = len(text), len(name)
    # fits >> j & 1: the name can be written from position j on, each of
    # its letters on that letter or on a "?"
    unknown = sum(1 << j for j, c in enumerate(text) if c == "?")
    mask = {}
    for j, c in enumerate(text):
        mask[c] = mask.get(c, unknown) | 1 << j
    fits = (1 << (n - m + 1)) - 1
    for i, c in enumerate(name):
        fits &= mask.get(c, unknown) >> i
    # two copies d < m apart agree exactly when d is a period of the name:
    # copies far apart never meet, and a set of copies agrees as soon as
    # each copy agrees with the next one, which covers what lies between
    border = [0] * m
    k = 0
    for i in range(1, m):
        while k and name[k] != name[i]:
            k = border[k - 1]
        if name[k] == name[i]:
            k += 1
        border[i] = k
    periods = []
    k = border[m - 1]
    while k:
        periods.append(m - k)
        k = border[k - 1]
    # best[j]: the most copies with the last one at j; before[j]: the most
    # with the last one before j
    best = [0] * (n - m + 1)
    before = [0] * (n - m + 2)
    for j in range(n - m + 1):
        if fits >> j & 1:
            far = before[j - m + 1] if j >= m else 0
            near = max((best[j - d] for d in periods if d <= j), default=0)
            best[j] = 1 + max(far, near)
        before[j + 1] = max(before[j], best[j])
    print(before[n - m + 1])


main()
