from os import _exit, write

DIGITS = 9
BASE = 10
FACTORIAL_EIGHT = 40320
OUTER_PAIR = 8
SECOND_PAIR = 14
THIRD_PAIR = 18
INNER_PAIR = 20


def count(target):
    # Complementing all nine digits maps sum S to81-S.
    reduced = min(target, DIGITS * (BASE - 1) - target)
    answer, choose_digits = 0, 1
    for excluded in range(reduced // BASE + 1):
        residual = reduced - BASE * excluded
        paired = residual * (residual + DIGITS)
        ways = (
            (paired + OUTER_PAIR)
            * (paired + SECOND_PAIR)
            * (paired + THIRD_PAIR)
            * (paired + INNER_PAIR)
        ) // FACTORIAL_EIGHT
        term = choose_digits * ways
        answer += -term if excluded & 1 else term
        choose_digits = choose_digits * (DIGITS - excluded) // (excluded + 1)
    return answer + (target == 1)


result = count(int(open(0, "rb", buffering=0).read()))
write(1, str(result).encode() + b"\n")
_exit(0)
