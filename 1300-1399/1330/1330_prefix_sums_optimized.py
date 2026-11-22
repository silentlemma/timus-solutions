import sys

BATCH_SIZE = 4096
INPUT_SIZE = 65536
WHITESPACE = 32


def numbers():
    pending = b""
    read = sys.stdin.buffer.read
    while True:
        block = read(INPUT_SIZE)
        if not block:
            break
        fields = (pending + block).split()
        pending = fields.pop() if block[-1] > WHITESPACE else b""
        yield from map(int, fields)
    if pending:
        yield int(pending)


def main():
    # Parse bounded blocks with C-level split/map, retaining only a partial token.
    values = numbers()
    n = next(values)
    # before[i] is the sum of the first i readings
    before = [0] * (n + 1)
    for i in range(1, n + 1):
        before[i] = before[i - 1] + next(values)
    answers = []
    for _ in range(next(values)):
        i, j = next(values), next(values)
        answers.append(str(before[j] - before[i - 1]))
        if len(answers) == BATCH_SIZE:
            sys.stdout.write("\n".join(answers) + "\n")
            answers.clear()
    if answers:
        sys.stdout.write("\n".join(answers) + "\n")


main()
