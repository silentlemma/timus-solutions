import os
import sys

INPUT_BUFFER_BYTES = 4096


def words():
    """Yield whitespace-separated tokens with bounded temporary storage."""
    pending = b""
    while True:
        block = os.read(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > 32 else b""
        yield from parts
    if pending:
        yield pending


def main():
    values = map(int, sys.stdin.buffer.read().split())
    month_count, d = next(values), next(values)
    # sell to everyone who can be served: by the end of month i at most
    # i * d yachts exist, so the running total of sales is capped there
    sales = []
    total = 0
    for i in range(1, month_count + 1):
        a = next(values)
        new = total + a
        capacity = i * d
        if new > capacity:
            new = capacity
        sales.append(new - total)
        total = new
    # build every yacht as late as possible: going backwards, whatever a
    # month cannot build is built earlier and waits one month per boundary
    carry = storage = 0
    for sold in reversed(sales):
        storage += carry
        carry = sold + carry - d
        if carry < 0:
            carry = 0
    print(total, storage)


main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
