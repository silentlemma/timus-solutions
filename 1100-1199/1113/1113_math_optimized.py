import sys

SCALE = 20000000


def exact_floor(load, stage):
    from fractions import Fraction

    total = Fraction(0)
    factor = load * (2 * stage - 1)
    for i in range(1, stage):
        denominator = 2 * i - 1
        total += Fraction(factor % denominator, denominator)
    return total.numerator // total.denominator


def line_ceiling(distance, load, stage):
    factor = load * (2 * stage - 1)
    whole = (stage - 1) * load + (2 * stage - 1) * distance
    lower = 0
    for i in range(1, stage):
        denominator = 2 * i - 1
        quotient, remainder = divmod(factor, denominator)
        whole -= quotient
        lower += remainder * SCALE // denominator
    floor = lower // SCALE
    # Each of stage-1 terms loses less than one scaled unit, strictly.
    if stage > 1 and (lower + stage - 2) // SCALE != floor:
        floor = exact_floor(load, stage)
    return whole - floor


def main():
    distance, load = map(int, sys.stdin.buffer.read().split())
    lower = 0
    stage = 1
    while lower + load * SCALE // (2 * stage - 1) < distance * SCALE:
        lower += load * SCALE // (2 * stage - 1)
        stage += 1
    # Lower-bound stage selection may overshoot by one, but never undershoots.
    answer = line_ceiling(distance, load, stage)
    if stage > 1:
        answer = max(answer, line_ceiling(distance, load, stage - 1))
    print(answer)


main()
