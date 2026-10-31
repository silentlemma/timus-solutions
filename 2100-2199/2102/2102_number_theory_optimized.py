TARGET = 20


def has_target_factors(n):
    remaining = TARGET
    divisor = 2
    while divisor * divisor <= n:
        # all remaining prime factors are at least divisor; Python powers are exact.
        if remaining > 2 and divisor**remaining > n:
            return False
        while n % divisor == 0:
            n //= divisor
            remaining -= 1
            if remaining == 0:
                return n == 1
        divisor += 1 if divisor == 2 else 2
    return remaining == (1 if n > 1 else 0)


print("Yes" if has_target_factors(int(input())) else "No")
