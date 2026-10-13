import sys

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# days from September 1 to the first day of each month
MONTHS = {"September": 0, "October": 30, "November": 61, "December": 91}


def main():
    first, month, day, a, b = sys.stdin.read().split()
    a, b = int(a), int(b)
    start = DAYS.index(first)
    match = MONTHS[month] + int(day) - 1  # September 1 is day 0
    count = [0] * len(DAYS)  # training days from September 2 to the eve of the match
    for i in range(1, match):
        count[(start + i) % len(DAYS)] += 1
    for mask in range(1, 1 << len(DAYS)):
        chosen = [d for d in range(len(DAYS)) if mask >> d & 1]
        if a <= sum(count[d] for d in chosen) <= b:
            print(len(chosen))
            print("\n".join(DAYS[d] for d in chosen))
            return
    print("Impossible")


main()
