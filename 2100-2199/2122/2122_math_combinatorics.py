import sys

MODULUS = 40961
ZERO = ord("0")


def main():
    bits = sys.stdin.buffer.read().strip()
    size = len(bits)
    row = [bit - ZERO for bit in bits]
    modulus = MODULUS
    factorial = 1
    for value in range(1, size + 1):
        factorial = factorial * value % modulus

    inverse_factorial = [1] * (size + 1)
    inverse_factorial[size] = pow(factorial, modulus - 2, modulus)
    for index in range(size, 0, -1):
        inverse_factorial[index - 1] = inverse_factorial[index] * index % modulus

    answer = [0] * (size + 1)
    total = 1
    ones_sum = sum(row)
    for length in range(size - 1, 0, -1):
        squares = 0
        # Scale counts by the factorial of the number of omitted positions.
        for index in range(length):
            value = ((length - index) * row[index] + (index + 1) * row[index + 1]) % modulus
            row[index] = value
            squares += value * value
        total = total * (length + 1) % modulus
        ones_sum = ones_sum * length % modulus
        inverse = inverse_factorial[size - length]
        answer[length] = (total * ones_sum - squares) * inverse * inverse % modulus

    print(" ".join(map(str, answer[1:])))


if __name__ == "__main__":
    main()
