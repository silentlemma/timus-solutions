import sys

MODULUS = 614889782588491410
ZERO = ord("0")


def process_queries(number, queries):
    digits = bytearray(number, "ascii")
    length = len(digits)
    weights = [1] * length
    for index in range(1, length):
        weights[index] = weights[index - 1] * 10 % MODULUS
    remainder = 0
    for digit in digits:
        remainder = (remainder * 10 + digit - ZERO) % MODULUS
    answers = []
    for query in queries:
        if query[0] == 0:
            answers.append(remainder % query[1])
        else:
            place, value = query[1:]
            index = length - place
            difference = value - (digits[index] - ZERO)
            digits[index] = value + ZERO
            remainder = (remainder + difference * weights[place - 1]) % MODULUS
    return answers


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    number = next(tokens).decode()
    count = int(next(tokens))
    queries = []
    for _ in range(count):
        kind = int(next(tokens))
        if kind == 0:
            queries.append((kind, int(next(tokens))))
        else:
            queries.append((kind, int(next(tokens)), int(next(tokens))))
    answers = process_queries(number, queries)
    sys.stdout.write("".join(f"{value}\n" for value in answers))


if __name__ == "__main__":
    main()
