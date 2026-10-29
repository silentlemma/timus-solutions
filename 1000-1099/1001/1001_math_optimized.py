import math
import sys

CHUNK_BYTES = 4096
SPACE_BYTE = ord(" ")

# the answers go out in blocks of about 4 KB of input, from the end, so the
# list of all square roots is never built at once
input_data = sys.stdin.buffer.read()
end = len(input_data)
while end > 0:
    start = max(0, end - CHUNK_BYTES)
    # move to a separator so a number never spans two blocks
    while start > 0 and input_data[start - 1] > SPACE_BYTE:
        start -= 1
    numbers = input_data[start:end].split()
    lines = ["%.4f" % math.sqrt(int(value)) for value in reversed(numbers)]
    if lines:
        sys.stdout.write("\n".join(lines) + "\n")
    end = start
