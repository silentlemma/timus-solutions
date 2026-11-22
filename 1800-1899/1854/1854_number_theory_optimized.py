from math import isqrt

FIRST_ODD_DIVISOR = 3
FIRST_WHEEL_DIVISOR = 5
WHEEL_PERIOD = 6


def square_part(value):
    root = isqrt(value)
    if root * root == value:
        return value
    answer = 1
    power = 0
    while value % FIRST_ODD_DIVISOR == 0:
        value //= FIRST_ODD_DIVISOR
        power += 1
    answer *= FIRST_ODD_DIVISOR ** (power - power % 2)
    root = isqrt(value)
    if root * root == value:
        return answer * value
    divisor = FIRST_WHEEL_DIVISOR
    step = 2
    while divisor * divisor * divisor <= value:
        power = 0
        while value % divisor == 0:
            value //= divisor
            power += 1
        if power:
            answer *= divisor ** (power - power % 2)
            root = isqrt(value)
            # A square residual is itself its largest square divisor.
            if root * root == value:
                return answer * value
        divisor += step
        step = WHEEL_PERIOD - step
    root = isqrt(value)
    return answer * value if root * root == value else answer


print(square_part(int(input())))
