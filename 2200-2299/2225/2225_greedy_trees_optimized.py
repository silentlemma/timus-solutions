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


def minimum_strikes(values):
    levels = []
    sizes = []
    answer = 0
    for height in values:
        right_size = 0
        while levels and levels[-1] >= height:
            previous = levels.pop()
            subtree = sizes.pop() + right_size
            parent = max(height, levels[-1] if levels else 0)
            # Joining two odd runs saves one strike at every remaining level.
            # Thus a component of length s costs ceil(s/2) per height layer;
            # this monotone stack folds the minimum Cartesian tree in one pass.
            answer += ((subtree + 1) // 2) * (previous - parent)
            right_size = subtree
        levels.append(height)
        sizes.append(right_size + 1)
    right_size = 0
    while levels:
        previous = levels.pop()
        subtree = sizes.pop() + right_size
        parent = levels[-1] if levels else 0
        answer += ((subtree + 1) // 2) * (previous - parent)
        right_size = subtree
    return answer


def main():
    values = map(int, words())
    count = next(values)
    print(minimum_strikes(next(values) for _ in range(count)))


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
