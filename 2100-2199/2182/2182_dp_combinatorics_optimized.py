from sys import stdin, stdout

BLOCK_SIZE = 1 << 16
OUTPUT_BATCH = 4096


def numbers():
    pending = b""
    while block := stdin.buffer.read(BLOCK_SIZE):
        tokens = (pending + block).split()
        pending = tokens.pop() if tokens and not block[-1:].isspace() else b""
        yield from map(int, tokens)
    if pending:
        yield int(pending)


def main():
    values = numbers()
    bits, _ = next(values), next(values)
    count = [0] * (bits + 1)
    combinations = 1
    for box in range(1, bits + 1):
        combinations = combinations * (bits - box + 1) // box
        count[box] = 1 + combinations - (box == 1)
    # Each small box sends its extra bottles to a single smaller box.
    for box in range(bits, 1, -1):
        count[box.bit_count()] += count[box] - 1
    answers = list(map(str, count))
    batch = []
    for box in values:
        batch.append(answers[box] if box <= bits else "1")
        if len(batch) == OUTPUT_BATCH:
            stdout.write(" ".join(batch) + " ")
            batch.clear()
    stdout.write(" ".join(batch) + "\n")


if __name__ == "__main__":
    main()
