import sys


def suffix_start(w, flip):
    # start of the lexicographically greatest suffix (the least one when
    # flip is set), by the comparison loop of the Two-Way algorithm
    n = len(w)
    best, j, k, p = -1, 0, 1, 1
    while j + k < n:
        a, b = w[j + k], w[best + k]
        if a != b and (a < b) != flip:
            j += k
            k = 1
            p = j - best
        elif a == b:
            if k != p:
                k += 1
            else:
                j += p
                k = 1
        else:
            best = j
            j = best + 1
            k = 1
            p = 1
    return best + 1


def main():
    w = sys.stdin.buffer.read().split()[0]
    n = len(w)
    # the longest border gives the period of the word
    border = [0] * n
    k = 0
    for i in range(1, n):
        c = w[i]
        while k and w[k] != c:
            k = border[k - 1]
        if w[k] == c:
            k += 1
        border[i] = k
    # the critical factorization theorem: the split before the later of
    # the two greatest suffixes has a local root as long as the period
    # (both are the whole word only for a power of one letter)
    split = max(suffix_start(w, False), suffix_start(w, True), 1)
    print(split, n - border[n - 1])


main()
