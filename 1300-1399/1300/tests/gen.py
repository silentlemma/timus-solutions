"""A tax scale and the amounts paid out: a seed and a mode. The salaries
are chosen first and the amounts are what an employer pays for them, so
every amount is reachable. Mode 1 gives small numbers, mode 2 a random
scale of up to 20 brackets and up to 30 employers, mode 3 the largest
sizes with amounts close to a billion."""

import random
import sys

CENTS = 100
BRACKETS = 20
EMPLOYERS = 30
TOP = 10**9 * CENTS
RATE = 99


def percent(amount, rate):
    return (amount * rate + CENTS // 2) // CENTS


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    small = mode == 1
    m = rng.randint(0, 3) if small else BRACKETS if mode == 3 else rng.randint(0, BRACKETS)
    high = 1000 * CENTS if small else TOP // 2
    limits = sorted(rng.sample(range(1, high), m))
    rates = [rng.randint(0, RATE) for _ in range(m + 1)]
    bonus_rate = rng.randint(0, RATE)

    def tax(amount):
        raw, previous = 0, 0
        for limit, rate in zip(limits, rates):
            if amount <= limit:
                return (raw + (amount - previous) * rate + CENTS // 2) // CENTS
            raw += (limit - previous) * rate
            previous = limit
        return (raw + (amount - previous) * rates[-1] + CENTS // 2) // CENTS

    def net(gross):
        bonus = percent(gross, bonus_rate)
        return gross - tax(gross) + bonus - tax(bonus)

    count = rng.randint(1, 4) if small else EMPLOYERS if mode == 3 else rng.randint(1, EMPLOYERS)
    paid = []
    while len(paid) < count:
        amount = net(rng.randint(1, high))
        if 0 < amount <= TOP:
            paid.append(amount)

    def show(c):
        return "%d.%02d" % (c // CENTS, c % CENTS)

    print(bonus_rate)
    for limit, rate in zip(limits, rates):
        print(show(limit), rate)
    print(0, rates[-1])
    for amount in paid:
        print(show(amount))
    print(-1)


main()
