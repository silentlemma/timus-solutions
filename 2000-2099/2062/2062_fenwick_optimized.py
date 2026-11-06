from array import array
from math import isqrt
import re
from sys import stdin, stdout

OUTPUT_BATCH = 1024


def smallest_factors(size):
    factors = array("H", [0]) * (size + 1)
    for prime in range(2, isqrt(size) + 1):
        if factors[prime] == 0:
            for multiple in range(prime * prime, size + 1, prime):
                if factors[multiple] == 0:
                    factors[multiple] = prime
    return factors


def divisor_list(value, factors):
    divisors = [1]
    while value > 1:
        prime = factors[value] or value
        count = len(divisors)
        power = prime
        value //= prime
        while True:
            for i in range(count):
                divisors.append(divisors[i] * power)
            if value % prime:
                break
            value //= prime
            power *= prime
    return divisors


def main():
    read = stdin.buffer.readline
    size = int(read())
    initial = array("I", [0])
    initial.extend(int(match[0]) for match in re.finditer(rb"[0-9]+", read()))
    factors = smallest_factors(size)
    tree = array("q", [0]) * (size + 1)
    measured = array("q", [0]) * (size + 1)
    measurement_epoch = array("I", [0]) * (size + 1)
    epoch = 1
    output = []
    for _ in range(int(read())):
        fields = read().split()
        if fields[0] == b"1":
            particle = int(fields[1])
            if measurement_epoch[particle] != epoch:
                total = initial[particle]
                for divisor in divisor_list(particle, factors):
                    while divisor:
                        total += tree[divisor]
                        divisor &= divisor - 1
                measured[particle] = total
                measurement_epoch[particle] = epoch
            output.append(str(measured[particle]))
            if len(output) == OUTPUT_BATCH:
                stdout.write("\n".join(output) + "\n")
                output.clear()
        else:
            left, right, power = map(int, fields[1:])
            if power == 0:
                continue
            epoch += 1
            while left <= size:
                tree[left] += power
                left += left & -left
            right += 1
            while right <= size:
                tree[right] -= power
                right += right & -right
    if output:
        stdout.write("\n".join(output) + "\n")


main()
