BASE = 10


def smallest(n):
    # a zero digit makes the product zero: 10 is the smallest such number
    if n == 0:
        return str(BASE)
    if n == 1:
        return "1"
    # the largest digits first give the fewest digits; then sort them up
    digits = []
    for d in range(BASE - 1, 1, -1):
        while n % d == 0:
            digits.append(str(d))
            n //= d
    return "".join(reversed(digits)) if n == 1 else "-1"


print(smallest(int(input())))
