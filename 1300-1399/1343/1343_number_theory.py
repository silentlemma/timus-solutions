import sys

DIGITS = 12
BASES = (2, 3, 5, 7, 11, 13)  # enough for every number below 3 * 10^12


def is_prime(n):
    """Miller-Rabin with fixed bases, exact for all 12-digit numbers."""
    if n < 2:
        return False
    for p in BASES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d, s = d // 2, s + 1
    for a in BASES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def main():
    words = sys.stdin.read().split()
    count = int(words[0])
    prefix = "".join(words[1:])[:count]  # the digits, together or apart
    free = DIGITS - count
    base = int(prefix or "0") * 10**free
    if free == 0:
        number = base  # the whole number is given and is the answer
    else:
        number = next(base + s for s in range(10**free) if is_prime(base + s))
    print(str(number).zfill(DIGITS))


main()
