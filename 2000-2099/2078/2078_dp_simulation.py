from sys import stdin, stdout

FRAMES = 10
PINS = 10
MAX_LAST_ROLLS = 3
STATES = 4
INF = FRAMES * PINS * MAX_LAST_ROLLS + 1


def main():
    totals = list(map(int, stdin.read().split()))
    low, high = [0] + [INF] * (STATES - 1), [0] + [-1] * (STATES - 1)
    for total in totals[:-1]:
        next_low, next_high = [INF] * STATES, [-1] * STATES
        for state in range(STATES):
            if high[state] < 0:
                continue
            a, b = (state + 1) // 2, state // 2
            if total < PINS:
                next_low[0] = min(next_low[0], low[state] + total * (1 + b))
                next_high[0] = max(next_high[0], high[state] + total * (1 + a))
            else:
                next_low[1] = min(next_low[1], low[state] + PINS * (1 + b))
                next_high[1] = max(next_high[1], high[state] + PINS + (PINS - 1) * a + b)
                # A strike consumes the old first bonus, then owes two new ones.
                target, bonus = 2 + b, PINS * (1 + a)
                next_low[target] = min(next_low[target], low[state] + bonus)
                next_high[target] = max(next_high[target], high[state] + bonus)
        low, high = next_low, next_high
    last = totals[-1]
    answer_low, answer_high = INF, -1
    for state in range(STATES):
        if high[state] < 0:
            continue
        a, b = (state + 1) // 2, state // 2
        if last < PINS:
            lower, upper = b * last, a * last
        elif last <= 2 * PINS:
            lower, upper = PINS * b, PINS * a + b * (last - PINS)
        else:
            # More than20pins forces the last frame's first two rolls to be10.
            lower = upper = PINS * (a + b)
        answer_low = min(answer_low, low[state] + last + lower)
        answer_high = max(answer_high, high[state] + last + upper)
    stdout.write(str(answer_low) + " " + str(answer_high) + "\n")


main()
