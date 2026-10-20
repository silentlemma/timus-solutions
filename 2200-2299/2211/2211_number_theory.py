import math
import sys

MIN_SUM_FACTOR = 3
QUADRATIC_FACTOR = 4
AREA_MULTIPLE = 6


def count_triangles(area):
    if area % AREA_MULTIPLE:
        return 0

    divisors = [1]
    remaining = area
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 2
        previous = divisors[:]
        power = 1
        for _ in range(exponent):
            power *= prime
            divisors.extend(value * power for value in previous)
        prime += 1 if prime == 2 else 2
    if remaining > 1:
        divisors += [value * remaining for value in divisors] + [
            value * remaining * remaining for value in divisors
        ]
    divisors.sort()

    square = area * area
    answer = 0
    # Heron's variables satisfy x <= y <= z and xyz(x + y + z) = area squared.
    for index, x in enumerate(divisors):
        if MIN_SUM_FACTOR * x**QUADRATIC_FACTOR > square:
            break
        remaining = square // x
        left, right = index, len(divisors)
        while left < right:
            middle = (left + right) // 2
            y = divisors[middle]
            if y * y * (x + 2 * y) <= remaining:
                left = middle + 1
            else:
                right = middle
        for y in divisors[index:left]:
            if remaining % y:
                continue
            total = x + y
            discriminant = total * total + QUADRATIC_FACTOR * (remaining // y)
            root = math.isqrt(discriminant)
            if root * root == discriminant and (root - total) % 2 == 0:
                answer += 1
    return answer


if __name__ == "__main__":
    print(count_triangles(int(sys.stdin.buffer.read())))
