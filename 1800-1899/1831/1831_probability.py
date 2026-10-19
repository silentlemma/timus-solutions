import sys

BASE = 10
LOW = range(BASE)  # digits of the lower places
TOP = range(1, BASE)  # digits of the leading place


def carry_chance(digits, extra):
    # the chance that two random digits plus the incoming carry reach 10
    hits = sum(a + b + extra >= BASE for a in digits for b in digits)
    return hits / len(digits) ** 2


def pair_chance(digits, a, b):
    # the chance that one place shows the digits a and b in either order
    return (1 if a == b else 2) / len(digits) ** 2


def main():
    k = int(sys.stdin.read())
    # every place costs one written digit and one sum; a carry costs a mark
    # and, unless it leaves the last place, one more second to add it in,
    # a carry out of the last place is written as a digit
    expected = 2 * k
    carry = 0.0
    low = carry_chance(LOW, 0), carry_chance(LOW, 1)
    top = carry_chance(TOP, 0), carry_chance(TOP, 1)
    for place in range(k):
        chance = top if place == k - 1 else low
        carry = (1 - carry) * chance[0] + carry * chance[1]
        expected += 2 * carry
    # the first sum of two digits both above 1 takes a second more
    for a in range(2, BASE):
        for b in range(a, BASE):
            miss = (1 - pair_chance(LOW, a, b)) ** (k - 1) * (1 - pair_chance(TOP, a, b))
            expected += 1 - miss
    print(f"{expected:.8f}")


main()
