import sys


def calm_intervals(constants):
    intervals = [(0, 1)]
    for reference in reversed(constants):
        candidates = []
        for left, right in intervals:
            if right < 0:
                continue
            left = max(left, 0)
            candidates.append((reference - right, reference - left))
            candidates.append((reference + left, reference + right))
        candidates.sort()
        merged = []
        for left, right in candidates:
            if merged and left <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], right))
            else:
                merged.append((left, right))
        intervals = merged
    return intervals


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(tokens)
    intervals = calm_intervals([next(tokens) for _ in range(count)])
    print(len(intervals))
    for left, right in intervals:
        print(left, right)


if __name__ == "__main__":
    main()
