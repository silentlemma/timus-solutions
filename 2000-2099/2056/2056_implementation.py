import sys

LOW_MARK = 3
TOP_MARK = 5
DOUBLED_THRESHOLD = 9


def classify(count, total, lowest):
    if lowest == LOW_MARK:
        return "None"
    if lowest == TOP_MARK:
        return "Named"
    if 2 * total >= DOUBLED_THRESHOLD * count:
        return "High"
    return "Common"


def main():
    fields = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(fields)
    total, lowest = 0, TOP_MARK
    for _ in range(count):
        grade = next(fields)
        total += grade
        lowest = min(lowest, grade)
    print(classify(count, total, lowest))


if __name__ == "__main__":
    main()
