import sys

MODULUS = 1000000007


def settings_counts(size):
    ways = [0] * (size + 1)
    for count in range(1, size + 1):
        closed = 0
        coefficients = iter(ways[1:count])
        square = count * count
        for first, second in zip(coefficients, coefficients):
            closed = (closed * square + first * count + second) % MODULUS
        if (count - 1) % 2:
            closed = (closed * count + ways[count - 1]) % MODULUS
        ways[count] = count * (pow(count, count - 1, MODULUS) - closed) % MODULUS
    return ways


def main():
    size = int(sys.stdin.buffer.read())
    print(settings_counts(size)[size])


if __name__ == "__main__":
    main()
