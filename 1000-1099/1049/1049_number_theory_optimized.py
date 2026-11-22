DECIMAL = 10
FIRST_ODD = 3
FIRST_WHEEL = 5
WHEEL_PERIOD = 6


def main():
    exponents = {}
    for value in map(int, open(0, "rb", buffering=0).read().split()):
        twos = (value & -value).bit_length() - 1
        if twos:
            exponents[2] = exponents.get(2, 0) + twos
            value >>= twos
        power = 0
        while value % FIRST_ODD == 0:
            value //= FIRST_ODD
            power += 1
        if power:
            exponents[FIRST_ODD] = exponents.get(FIRST_ODD, 0) + power
        prime, step = FIRST_WHEEL, 2
        while prime * prime <= value:
            power = 0
            while value % prime == 0:
                value //= prime
                power += 1
            if power:
                exponents[prime] = exponents.get(prime, 0) + power
            prime += step
            step = WHEEL_PERIOD - step
        if value > 1:
            exponents[value] = exponents.get(value, 0) + 1
    answer = 1
    for power in exponents.values():
        answer = answer * (power + 1) % DECIMAL
    open(1, "wb", buffering=0).write(bytes((ord("0") + answer, ord("\n"))))


main()
