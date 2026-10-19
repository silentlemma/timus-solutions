import sys

TOTAL_TASKS = 12
FIRST_HOUR_MINUTES = 60
MINUTES_PER_TASK = 45
CONTEST_MINUTES = 300


def solve(first_hour):
    return FIRST_HOUR_MINUTES + (TOTAL_TASKS - first_hour) * MINUTES_PER_TASK <= CONTEST_MINUTES


if __name__ == "__main__":
    first_hour = int(sys.stdin.buffer.read())
    print("YES" if solve(first_hour) else "NO")
