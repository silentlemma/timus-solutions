import sys

CHUNK_SIZE = 1 << 16
UNKNOWN = -1
WHITESPACE = b" \t\n\r\v\f"


def integers():
    pending = b""
    while True:
        chunk = sys.stdin.buffer.read(CHUNK_SIZE)
        if not chunk:
            break
        fields = (pending + chunk).split()
        if chunk[-1] in WHITESPACE:
            pending = b""
        else:
            pending = fields.pop()
        yield from map(int, fields)
    if pending:
        yield int(pending)


def main():
    values = integers()
    n = next(values)
    remaining = n - 2
    fixed_weight = 0
    unknown_count = 0
    unknown_sum = 0
    for vertex, degree in enumerate(values, 1):
        if degree == UNKNOWN:
            unknown_count += 1
            unknown_sum += vertex
        else:
            remaining -= degree - 1
            fixed_weight += vertex * (degree - 1)

    answer = n * (n + 1) // 2 + n * fixed_weight
    if unknown_count:
        quotient, remainder = divmod(remaining * unknown_sum, unknown_count)
        answer += n * quotient + n * remainder // unknown_count
    print(answer)


if __name__ == "__main__":
    main()
