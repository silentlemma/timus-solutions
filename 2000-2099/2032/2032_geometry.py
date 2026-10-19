from math import gcd, isqrt
import sys

FIRST_ODD = 3
MIN_HYPOTENUSE = 5


def divisors(number):
    values = [1]
    prime = 2
    while prime * prime <= number:
        previous = list(values)
        power = 1
        while number % prime == 0:
            number //= prime
            power *= prime
            values.extend(value * power for value in previous)
        prime = FIRST_ODD if prime == 2 else prime + 2
    if number > 1:
        values.extend(value * number for value in list(values))
    return values


def solve(sides):
    radius, length, opposite = sorted(sides)
    twice_dot = radius * radius + length * length - opposite * opposite
    if twice_dot % 2:
        return None
    dot = twice_dot // 2
    square = radius * radius * length * length - dot * dot
    if square < 0:
        return None
    cross = isqrt(square)
    if cross * cross != square:
        return None
    denominator = radius * radius

    def point(x, y):
        u, v = dot * x - cross * y, dot * y + cross * x
        if u % denominator or v % denominator:
            return None
        return [0, 0, x, y, u // denominator, v // denominator]

    answer = point(radius, 0) or point(0, radius)
    if answer:
        return answer
    for hypotenuse in divisors(radius):
        if hypotenuse < MIN_HYPOTENUSE or hypotenuse % 2 == 0:
            continue
        for m in range(isqrt(hypotenuse // 2) + 1, isqrt(hypotenuse - 1) + 1):
            rest = hypotenuse - m * m
            k = isqrt(rest)
            if k * k != rest or gcd(m, k) != 1 or (m - k) % 2 == 0:
                continue
            scale = radius // hypotenuse
            x, y = scale * (m * m - k * k), scale * 2 * m * k
            answer = point(x, y) or point(y, x)
            if answer:
                return answer
    return None


def main():
    sides = list(map(int, sys.stdin.buffer.read().split()))
    if not sides:
        return
    answer = solve(sides)
    if answer is None:
        print(-1)
    else:
        for i in range(0, len(answer), 2):
            print(answer[i], answer[i + 1])


if __name__ == "__main__":
    main()
