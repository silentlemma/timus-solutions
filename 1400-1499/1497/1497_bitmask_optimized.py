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


def slides_up(black, seen_white):
    """The black piece can slide up: no white cell above a black one."""
    return not (black & seen_white)


def main():
    tokens = words()
    n = int(next(tokens))
    mask = (1 << n) - 1
    seen_black = seen_white = 0
    # a sliding direction for either piece is the opposite one for the
    # other; a diagonal slide works only if both of its axis slides do, so
    # trying the four axis directions for the black piece is enough
    up = down = left = right = True
    for _ in range(n):
        row = next(tokens)
        black = int(row, 2)
        white = mask ^ black
        up = up and slides_up(black, seen_white)
        down = down and slides_up(white, seen_black)
        seen_black |= black
        seen_white |= white
        left = left and b"01" not in row
        right = right and b"10" not in row
    print("Yes" if up or down or left or right else "No")


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
