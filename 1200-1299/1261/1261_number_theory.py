BASE = 3


def main():
    n = int(input())
    # balanced ternary: digits 1 go into the payment, digits -1 into the tip
    pay, tip, power = 0, 0, 1
    while n:
        if n % BASE == 1:
            pay += power
            n -= 1
        elif n % BASE == BASE - 1:
            tip += power
            n += 1
        n //= BASE
        power *= BASE
    # no tip yet: add the smallest bill the payment lacks to both
    power = 1
    while tip == 0:
        if pay // power % BASE == 0:
            pay += power
            tip = power
        power *= BASE
    print(pay, tip)


main()
