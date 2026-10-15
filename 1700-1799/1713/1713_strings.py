import sys


def common(a, b):
    # the longest common prefix, by binary search over slice comparisons
    lo, hi = 0, min(len(a), len(b))
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if a[:mid] == b[:mid]:
            lo = mid
        else:
            hi = mid - 1
    return lo


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    words = data[1:1 + n]
    # every suffix of every command, sorted; a substring starting at some
    # position is in another command exactly when it is a prefix of another
    # command's suffix, and the nearest such suffixes in the order share most
    suffixes = sorted((w[p:], i, p) for i, w in enumerate(words) for p in range(len(w)))
    total = len(suffixes)
    adjacent = [common(suffixes[k][0], suffixes[k + 1][0]) for k in range(total - 1)]
    shared = [0] * total  # the longest prefix shared with another command
    run = 0
    for k in range(1, total):
        if suffixes[k][1] != suffixes[k - 1][1]:
            run = adjacent[k - 1]
        else:
            run = min(run, adjacent[k - 1])
        shared[k] = run
    run = 0
    for k in range(total - 2, -1, -1):
        if suffixes[k][1] != suffixes[k + 1][1]:
            run = adjacent[k]
        else:
            run = min(run, adjacent[k])
        shared[k] = max(shared[k], run)
    best = [None] * n
    for k, (suffix, i, p) in enumerate(suffixes):
        need = shared[k] + 1
        if need <= len(suffix) and (best[i] is None or need < len(best[i])):
            best[i] = suffix[:need]
    print("\n".join(best))


main()
