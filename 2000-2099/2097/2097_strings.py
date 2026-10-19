import sys

NONE = -1


def second_differences(h):
    return [h[i + 2] - 2 * h[i + 1] + h[i] for i in range(len(h) - 2)]


def prefix_function(p):
    pi = [0] * len(p)
    for i in range(1, len(p)):
        k = pi[i - 1]
        while k and p[i] != p[k]:
            k = pi[k - 1]
        if p[i] == p[k]:
            k += 1
        pi[i] = k
    return pi


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    x = data[2:2 + m + 1]
    pos = 2 + m + 1
    # a section is similar exactly when the second differences agree, and then
    # a is the difference of the first steps of the two sections
    pattern = second_differences(x)
    pi = prefix_function(pattern)
    best = None  # (|a|, slope, start)
    for slope in range(1, n + 1):
        length = data[pos]
        y = data[pos + 1:pos + 2 + length]
        pos += 2 + length
        if length < m:
            continue
        text = second_differences(y)
        k = 0
        for i in range(len(text) + 1):
            if k == len(pattern):
                start = i - len(pattern)
                a = abs((x[1] - x[0]) - (y[start + 1] - y[start]))
                if best is None or a < best[0]:
                    best = (a, slope, start)
                if pattern:
                    k = pi[k - 1]
            if i == len(text):
                break
            if not pattern:
                continue
            while k and text[i] != pattern[k]:
                k = pi[k - 1]
            if text[i] == pattern[k]:
                k += 1
    print(NONE if best is None else "%d %d" % (best[1], best[2]))


main()
