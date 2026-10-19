from array import array
import math
import sys

MAX_MINUTES = 300
MAX_DIVISOR = MAX_MINUTES + 1
WHEEL_PRIMES = 6


def build_tables():
    limit = MAX_DIVISOR * MAX_DIVISOR
    prime = bytearray(b"\x01") * (limit + 1)
    prime[:2] = b"\x00\x00"
    for divisor in range(2, math.isqrt(limit) + 1):
        if prime[divisor]:
            start = divisor * divisor
            prime[start::divisor] = b"\x00" * ((limit - start) // divisor + 1)
    counts = array("I", [0]) * (limit + 1)
    total = 0
    for number in range(limit + 1):
        total += prime[number]
        counts[number] = total
    primes = tuple(number for number in range(2, MAX_DIVISOR + 1) if prime[number])
    wheels = [(1, array("H", [0, 1]))]
    period = 1
    for used in range(1, WHEEL_PRIMES + 1):
        period *= primes[used - 1]
        survives = bytearray(b"\x01") * (period + 1)
        survives[0] = 0
        for divisor in primes[:used]:
            survives[divisor::divisor] = b"\x00" * (period // divisor)
        prefix = array("H", [0])
        total = 0
        for number in range(1, period + 1):
            total += survives[number]
            prefix.append(total)
        wheels.append((period, prefix))
    return primes, counts, wheels


SMALL_PRIMES, PRIME_COUNTS, WHEELS = build_tables()
USED_BITS = len(SMALL_PRIMES).bit_length()


def count_years(start, duration, minutes):
    limit = minutes + 1
    used = PRIME_COUNTS[limit]
    base = min(used, WHEEL_PRIMES)
    period, prefix = WHEELS[base]
    per_period = prefix[-1]
    memo = {}

    def phi(value, remaining):
        if remaining == base:
            return value // period * per_period + prefix[value % period]
        if value == 0:
            return 0
        last = SMALL_PRIMES[remaining - 1]
        if value < last:
            return 1
        if value < last * last:
            return 1 + PRIME_COUNTS[value] - remaining
        key = (value << USED_BITS) | remaining
        cached = memo.get(key)
        if cached is not None:
            return cached
        result = phi(value, remaining - 1) - phi(value // last, remaining - 1)
        memo[key] = result
        return result

    finish = start + duration
    result = phi(finish, used) - phi(start, used)
    result += PRIME_COUNTS[min(finish, limit)] - PRIME_COUNTS[min(start, limit)]
    memo.clear()
    return result


if __name__ == "__main__":
    start, duration, minutes = map(int, sys.stdin.buffer.read().split())
    print(count_years(start, duration, minutes))
