import sys


def main():
    data = iter(map(int, sys.stdin.read().split()))
    n = next(data)
    students = sorted((next(data), next(data), next(data)) for _ in range(n))
    # moving the start earlier changes nobody's order or wait, it only adds
    # the same amount to every deadline: the answer is the worst lateness
    busy_until, worst = 0, 0
    for ready, talk, deadline in students:
        busy_until = max(busy_until, ready) + talk
        worst = max(worst, busy_until - deadline)
    print(worst)


main()
