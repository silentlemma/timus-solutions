import sys

PARAMETER_COUNT = 8


def minimum_energy(
    speed, length, fire_speed, fire_width, gap, natural, shield, braking, branches
):
    difference = fire_speed - speed
    best = float("inf")
    for left, right in branches:
        entry = left + length
        distance = right - entry
        held = entry * difference - gap * speed
        shield_numerator = max(0, held) * shield
        shield_denominator = speed * difference
        delay_numerator = speed * (right - left + fire_width) + max(0, -held)
        if delay_numerator >= 2 * distance * fire_speed:
            brake_numerator = speed * speed
            brake_denominator = 2 * distance
        elif delay_numerator <= distance * fire_speed:
            brake_numerator = 0
            brake_denominator = 1
        else:
            brake_numerator = (
                2
                * speed
                * speed
                * fire_speed
                * (delay_numerator - distance * fire_speed)
            )
            brake_denominator = delay_numerator * delay_numerator
        extra = max(0, brake_numerator - natural * brake_denominator)
        cost = (
            shield_numerator / shield_denominator + braking * extra / brake_denominator
        )
        best = min(best, cost)
    return best


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    parameters = values[:PARAMETER_COUNT]
    count = values[PARAMETER_COUNT]
    offset = PARAMETER_COUNT + 1
    branches = list(zip(values[offset::2], values[offset + 1 :: 2]))
    print(f"{minimum_energy(*parameters, branches[:count]):.12f}")


if __name__ == "__main__":
    main()
