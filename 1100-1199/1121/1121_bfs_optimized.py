import os
from array import array
import sys

INPUT_BUFFER_BYTES = 4096
MAX_ASCII_WHITESPACE = 32
UNREACHED_DISTANCE = 255

REACH = 5


def words():
    """Yield whitespace-separated tokens with bounded temporary storage."""
    pending = b""
    while True:
        block = os.read(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > MAX_ASCII_WHITESPACE else b""
        yield from parts
    if pending:
        yield pending


def main():
    values = map(int, words())
    h, w = next(values), next(values)
    cells = h * w
    labels = array("H", (next(values) for _ in range(cells)))
    distance = bytearray([UNREACHED_DISTANCE]) * cells
    queue = array("I")
    for index, mask in enumerate(labels):
        if mask:
            distance[index] = 0
            queue.append(index)
    # FIFO order processes every distance layer before expanding the next.
    # Equal-distance parents merge branch types before a cell expands.
    head = 0
    while head < len(queue):
        vertex = queue[head]
        head += 1
        following = distance[vertex] + 1
        if following > REACH:
            continue
        column = vertex % w
        for neighbor in (
            vertex - w,
            vertex + w,
            vertex - 1 if column else -1,
            vertex + 1 if column + 1 < w else cells,
        ):
            if 0 <= neighbor < cells:
                if distance[neighbor] == UNREACHED_DISTANCE:
                    distance[neighbor] = following
                    labels[neighbor] = labels[vertex]
                    queue.append(neighbor)
                elif distance[neighbor] == following:
                    # each type counts once however many branches share it
                    labels[neighbor] |= labels[vertex]
    write = sys.stdout.write
    for start in range(0, cells, w):
        write(
            " ".join(
                "-1" if distance[index] == 0 else str(labels[index])
                for index in range(start, start + w)
            )
            + "\n"
        )


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
