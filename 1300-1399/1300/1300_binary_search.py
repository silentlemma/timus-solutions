import sys

CENTS = 100
DIGITS = 2


def cents(token):
    """A non-negative amount with at most two decimals, in cents."""
    whole, _, frac = token.partition(".")
    return int(whole or "0") * CENTS + int((frac + "0" * DIGITS)[:DIGITS])


def main():
    lines = [line.split() for line in sys.stdin.read().splitlines() if line.strip()]
    bonus_rate = int(lines[0][0])
    limits, rates = [], []
    row = 1
    while True:
        limit, rate = cents(lines[row][0]), int(lines[row][1])
        row += 1
        if limit == 0:
            top_rate = rate
            break
        limits.append(limit)
        rates.append(rate)
    paid = []
    while lines[row][0] != "-1":
        paid.append(cents(lines[row][0]))
        row += 1

    def percent(amount, rate):
        # rate percent of an amount in cents, rounded half up to a cent
        return (amount * rate + CENTS // 2) // CENTS

    def tax(amount):
        raw, previous = 0, 0
        for limit, rate in zip(limits, rates):
            if amount <= limit:
                return (raw + (amount - previous) * rate + CENTS // 2) // CENTS
            raw += (limit - previous) * rate
            previous = limit
        return (raw + (amount - previous) * top_rate + CENTS // 2) // CENTS

    def net(gross):
        bonus = percent(gross, bonus_rate)
        return gross - tax(gross) + bonus - tax(bonus)

    def gross_for(amount):
        # net never decreases as the salary grows, so the largest salary
        # whose net does not exceed the amount paid is found by bisection
        lo, hi = 0, 1
        while net(hi) <= amount:
            hi *= 2
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if net(mid) <= amount:
                lo = mid
            else:
                hi = mid
        return lo

    total, withheld = 0, 0
    for amount in paid:
        gross = gross_for(amount)
        total += gross
        withheld += tax(gross) + tax(percent(gross, bonus_rate))
    owed = tax(total) + tax(percent(total, bonus_rate)) - withheld
    sign = "-" if owed < 0 else ""
    print("%s%d.%02d" % (sign, abs(owed) // CENTS, abs(owed) % CENTS))


main()
