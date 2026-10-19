import sys


FACTOR_LIMIT = 100
LOW_FPS = 10
HIGH_FPS = 60


def factor_table():
    factors = [[] for _ in range(FACTOR_LIMIT + 1)]
    primes = []
    for value in range(2, FACTOR_LIMIT + 1):
        remaining = value
        for prime in primes:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            if exponent:
                factors[value].append((prime, exponent))
        if remaining > 1:
            factors[value].append((remaining, 1))
            if remaining == value:
                primes.append(value)
    return primes, factors


def classify(width, height, power, counts, primes):
    area = width * height
    limit = power // (LOW_FPS * area)
    if limit == 0:
        return 'Slideshow'
    product = 1
    for prime in primes:
        for _ in range(counts[prime]):
            if product > limit // prime:
                return 'Slideshow'
            product *= prime
    return 'Perfect' if product <= power // (HIGH_FPS * area) else 'So-so'


def main():
    read = sys.stdin.buffer.readline
    primes, factors = factor_table()
    options = {}
    counts = [0] * (FACTOR_LIMIT + 1)
    for _ in range(int(read())):
        name, text = read().split()
        value = int(text)
        options[name] = value
        for prime, exponent in factors[value]:
            counts[prime] += exponent
    width, height, power = map(int, read().split())
    answer = [classify(width, height, power, counts, primes)]
    for _ in range(int(read())):
        command = read().split()
        if command[0] == b'Resolution':
            width, height = map(int, command[1:])
        else:
            change = 1 if command[0] == b'On' else -1
            for prime, exponent in factors[options[command[1]]]:
                counts[prime] += change * exponent
        answer.append(classify(width, height, power, counts, primes))
    sys.stdout.write('\n'.join(answer) + '\n')


if __name__ == '__main__':
    main()
