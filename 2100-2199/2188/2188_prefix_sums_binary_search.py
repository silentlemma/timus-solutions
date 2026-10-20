import sys
from bisect import bisect_right


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    q = next(data)
    gain = [next(data) for _ in range(n)]
    total = 0
    for i in range(n):
        total += gain[i] - next(data)
        gain[i] = total

    suffix = [0] * n
    minimum = gain[-1]
    for i in range(n - 1, -1, -1):
        value = gain[i]
        if value < minimum:
            minimum = value
        suffix[i] = minimum

    thresholds = []
    times = []
    peak = 0
    for i, value in enumerate(gain):
        # Avoiding an earlier overtake loses max(0, peak - distance) feet.
        if suffix[i] > peak:
            thresholds.append(suffix[i])
            times.append(i + 1)
        if value > peak:
            peak = value

    answers = []
    count = len(times)
    for _ in range(q):
        position = bisect_right(thresholds, next(data))
        answers.append(str(times[position]) if position < count else "-1")
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
