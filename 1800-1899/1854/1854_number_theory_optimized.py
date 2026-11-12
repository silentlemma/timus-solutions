from math import isqrt

FIRST_ODD_DIVISOR = 3


def square_part(value):
    root = isqrt(value)
    if root * root == value:
        return value
    answer = 1
    divisor = FIRST_ODD_DIVISOR
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
        divisor += 2
    root = isqrt(value)
    return answer * value if root * root == value else answer


print(square_part(int(input())))
