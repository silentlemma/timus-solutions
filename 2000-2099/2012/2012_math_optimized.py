import sys

TOTAL_TASKS = 12
FIRST_HOUR_MINUTES = 60
MINUTES_PER_TASK = 45
CONTEST_MINUTES = 300

first_hour = int(sys.stdin.buffer.read())
finish = FIRST_HOUR_MINUTES + (TOTAL_TASKS - first_hour) * MINUTES_PER_TASK
print("YES" if finish <= CONTEST_MINUTES else "NO")
