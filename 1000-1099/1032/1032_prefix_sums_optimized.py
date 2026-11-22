import os
from array import array
from sys import stdin, stdout

OUTPUT_CHUNK = 512


def main():
    read = stdin.buffer
    size = int(read.readline())
    first = array("H", [0]) * size
    first[0] = 1
    values = array("H")
    remainder = 0
    for line in read:
        for token in line.split():
            value = int(token)
            values.append(value)
            remainder = (remainder + value) % size
            start = first[remainder]
            if start:
                # N <= 10000 and every value <= 15000 fit unsigned shorts.
                stdout.write(f"{len(values) - start + 1}\n")
                for begin in range(start - 1, len(values), OUTPUT_CHUNK):
                    stdout.write("\n".join(map(str, values[begin : begin + OUTPUT_CHUNK])) + "\n")
                stdout.flush()
                os._exit(0)
            first[remainder] = len(values) + 1


main()
