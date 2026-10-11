import sys


def main():
    data = sys.stdin.buffer.read().split()
    m = int(data[0])
    segments = []
    for i in range(1, len(data) - 1, 2):
        left, right = int(data[i]), int(data[i + 1])
        if left == 0 and right == 0:
            break
        segments.append((left, right))
    segments.sort()
    chosen = []
    covered, i = 0, 0
    while covered < m:
        # among the segments that start inside the covered part, take the
        # one that reaches furthest; it is never worse than any other
        best = None
        while i < len(segments) and segments[i][0] <= covered:
            if best is None or segments[i][1] > best[1]:
                best = segments[i]
            i += 1
        if best is None or best[1] <= covered:
            print("No solution")
            return
        chosen.append(best)
        covered = best[1]
    out = [str(len(chosen))] + ["%d %d" % s for s in chosen]
    print("\n".join(out))


main()
