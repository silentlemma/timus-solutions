import os
from array import array
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
    values = iter(map(int, words()))
    floors, elevators = next(values), next(values)
    difference = array("i", [0]) * (floors + 1)
    for left, right in zip(values, values):
        difference[left] += 1
        difference[right] -= 1
    if floors == 1:
        print(-1)
        return

    crossing = 0
    answer = elevators
    # Every route crosses each gap; cover all elevators crossing the cheapest gap.
    for floor in range(1, floors):
        crossing += difference[floor]
        if crossing < answer:
            answer = crossing
    print(answer)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
