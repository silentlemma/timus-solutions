import sys

MAX_VALUE = 100


def make_hull(lines):
    hull = []
    for slope, intercept in sorted(lines):
        if hull and hull[-1][0] == slope:
            if hull[-1][1] >= intercept:
                continue
            hull.pop()
        while len(hull) >= 2:
            a, b = hull[-2], hull[-1]
            if (a[1] - b[1]) * (slope - b[0]) < (b[1] - intercept) * (b[0] - a[0]):
                break
            hull.pop()
        hull.append((slope, intercept))
    return hull


def maximum(hull, day):
    left, right = 0, len(hull) - 1
    while left < right:
        middle = (left + right) // 2
        a, b = hull[middle], hull[middle + 1]
        if a[0] * day + a[1] <= b[0] * day + b[1]:
            left = middle + 1
        else:
            right = middle
    slope, intercept = hull[left]
    return slope * day + intercept


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(data)
    best = [0] * (MAX_VALUE + 1)
    for _ in range(count):
        cost, income = next(data), next(data)
        best[cost] = max(best[cost], income)

    options = []
    peak = 0
    for cost in range(1, MAX_VALUE + 1):
        if best[cost] > peak:
            peak = best[cost]
            options.append((cost, peak))
    cap, top_income = options[-1]
    length = cap + 1
    state_count = cap + 2 * top_income + 1
    current = [-1] * state_count
    current[0] = 0
    work_events = []
    rich = []
    day = 0
    while any(money >= 0 for money in current):
        following = [-1] * state_count
        events = []
        greatest = -1
        for income in range(state_count - 1, -1, -1):
            money = current[income]
            if money <= greatest:
                continue
            greatest = money
            if income >= cap and money >= cap:
                rich.append((day, income, money))
                continue
            events.append((income + 1, money - (income + 1) * day))
            # Once every price is affordable, move the next purchase before any work.
            if money < cap:
                following[income] = max(following[income], money + income + 1)
            for cost, extra in options:
                if cost > money:
                    break
                target = income + extra
                following[target] = max(following[target], money - cost + income)
        work_events.append(events)
        current = following
        day += 1

    limit = len(work_events) - 1 + length
    suffix = [0] * (limit + 1)
    for remaining in range(limit):
        gain = max(1, max(income * remaining - cost for cost, income in options))
        suffix[remaining + 1] = suffix[remaining] + gain
    correction = suffix[length] - top_income * length * (length - 1) // 2 + cap * length

    answers = [0] * (limit + 1)
    work_best = [None] * state_count
    for horizon in range(limit + 1):
        if horizon < len(work_events):
            for slope, intercept in work_events[horizon]:
                previous = work_best[slope]
                if previous is None or intercept > previous:
                    work_best[slope] = intercept
        answers[horizon] = max(
            slope * horizon + intercept
            for slope, intercept in enumerate(work_best)
            if intercept is not None
        )

    lines = []
    for start, income, money in rich:
        for remaining in range(limit - start + 1):
            horizon = start + remaining
            candidate = money + income * remaining + suffix[remaining]
            if candidate > answers[horizon]:
                answers[horizon] = candidate
        slope = income - top_income * start
        intercept = money - income * start + top_income * start * (start + 1) // 2
        lines.append((slope, intercept + cap * start + correction))
    rich_hull = make_hull(lines)
    work_hull = make_hull(
        (slope, intercept) for slope, intercept in enumerate(work_best) if intercept is not None
    )

    count = next(data)
    output = []
    for _ in range(count):
        horizon = next(data)
        if horizon <= limit:
            answer = answers[horizon]
        else:
            common = top_income * horizon * (horizon - 1) // 2 - cap * horizon
            answer = max(maximum(work_hull, horizon), common + maximum(rich_hull, horizon))
        output.append(str(answer))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
