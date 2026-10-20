import sys
from array import array


MODULUS = 998244353
PRIMITIVE_ROOT = 3
BLOCK_SIZE = 100000


def make_roots(size):
    roots = array("I", [0]) * size
    roots[1] = 1
    length = 2
    while length < size:
        step = pow(PRIMITIVE_ROOT, (MODULUS - 1) // (length * 2), MODULUS)
        for index in range(length // 2, length):
            roots[index * 2] = roots[index]
            roots[index * 2 + 1] = roots[index] * step % MODULUS
        length *= 2
    return roots


def forward_transform(values, roots):
    size = len(values)
    half = size // 2
    while half:
        for start in range(0, size, half * 2):
            for offset in range(half):
                first = values[start + offset]
                second = values[start + offset + half]
                addition = first + second
                if addition >= MODULUS:
                    addition -= MODULUS
                difference = first - second
                if difference < 0:
                    difference += MODULUS
                values[start + offset] = addition
                values[start + offset + half] = difference * roots[half + offset] % MODULUS
        half //= 2


def reverse_transform(values, roots):
    size = len(values)
    half = 1
    while half < size:
        for start in range(0, size, half * 2):
            for offset in range(half):
                first = values[start + offset]
                second = values[start + offset + half] * roots[half + offset] % MODULUS
                addition = first + second
                if addition >= MODULUS:
                    addition -= MODULUS
                difference = first - second
                if difference < 0:
                    difference += MODULUS
                values[start + offset] = addition
                values[start + offset + half] = difference
        half *= 2


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[:2]
    values = data[2:]
    del data
    total = n + m

    if all(value == values[0] for value in values):
        sys.stdout.write(" ".join([str(values[0])] * m) + "\n")
        return

    inverses = array("I", [0, 1])
    for value in range(2, total):
        inverses.append(MODULUS - MODULUS // value * inverses[MODULUS % value] % MODULUS)

    factorial = 1
    inverse_factorials = array("I", [1])
    for value in range(1, n):
        factorial = factorial * value % MODULUS
        inverse_factorials.append(inverse_factorials[-1] * inverses[value] % MODULUS)

    size = 1
    while size < n + total - 1:
        size *= 2
    weights = array("I", [0]) * size
    # Lagrange weights turn evaluation at consecutive points into a convolution.
    for index, value in enumerate(values):
        weight = value * inverse_factorials[index] % MODULUS
        weight = weight * inverse_factorials[n - 1 - index] % MODULUS
        if (n - 1 - index) % 2:
            weight = -weight % MODULUS
        weights[index] = weight
    del values, inverse_factorials

    roots = make_roots(size)
    kernel = inverses[:]
    kernel.extend(array("I", [0]) * (size - total))
    forward_transform(weights, roots)
    forward_transform(kernel, roots)
    for index in range(size):
        weights[index] = weights[index] * kernel[index] % MODULUS
    del kernel
    reverse_transform(weights, roots)
    del roots

    # Reusing the forward roots reverses the coefficients and leaves a size factor.
    scale = factorial * n % MODULUS * pow(size, MODULUS - 2, MODULUS) % MODULUS
    chunks = []
    for begin in range(n, total, BLOCK_SIZE):
        end = min(total, begin + BLOCK_SIZE)
        output = []
        for current in range(begin, end):
            output.append(str(weights[size - current] * scale % MODULUS))
            scale = scale * (current + 1) % MODULUS * inverses[current - n + 1] % MODULUS
        chunks.append(" ".join(output))
    sys.stdout.write(" ".join(chunks) + "\n")


if __name__ == "__main__":
    main()
