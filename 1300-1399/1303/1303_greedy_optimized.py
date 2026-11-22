import sys


def main():
    source = sys.stdin.buffer
    m = int(source.readline())
    left, right = [0] * m, [0] * m
    # starts at or below zero share bucket zero; only the farthest end matters.
    # m <= 5000 bounds storage independently of the number of intervals.
    for line in source:
        start, end = map(int, line.split())
        if start == end == 0:
            break
        if start >= m or end <= 0:
            continue
        at = max(0, start)
        if end > right[at] or (end == right[at] and start < left[at]):
            left[at], right[at] = start, end
    chosen = []
    covered = at = 0
    while covered < m:
        # among the segments that start inside the covered part, take the
        # one that reaches furthest; it is never worse than any other
        best = -1
        while at < m and at <= covered:
            if best < 0 or right[at] > right[best]:
                best = at
            at += 1
        if best < 0 or right[best] <= covered:
            print("No solution")
            return
        chosen.append(f"{left[best]} {right[best]}")
        covered = right[best]
    print(len(chosen))
    print("\n".join(chosen))


main()
