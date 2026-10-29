import sys
from array import array

OUTPUT_BATCH = 256


def main():
    numbers = (int(token) for line in sys.stdin.buffer for token in line.split())
    width = next(numbers)
    # the window keeps values decreasing from front to back, so the front is the
    # maximum; it is a circular buffer of two int arrays instead of a deque,
    # and the answers go out in batches of 256 lines
    values = array("i", [0]) * width
    indices = array("i", [0]) * width
    head = size = 0
    output = []
    for index, value in enumerate(numbers):
        if value < 0:
            break
        if size and indices[head] <= index - width:
            head = (head + 1) % width
            size -= 1
        while size and values[(head + size - 1) % width] <= value:
            size -= 1
        tail = (head + size) % width
        values[tail], indices[tail] = value, index
        size += 1
        if index + 1 >= width:
            output.append(str(values[head]))
            if len(output) == OUTPUT_BATCH:
                sys.stdout.write("\n".join(output) + "\n")
                output.clear()
    if output:
        sys.stdout.write("\n".join(output) + "\n")


main()
