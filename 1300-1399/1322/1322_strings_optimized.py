import sys
from array import array

CHARS = 128
CHAR_BITS = 7


def main():
    words = sys.stdin.buffer.read().split()
    row, last = int(words[0]) - 1, words[1]
    # a stable counting sort of the last column: the row packed in order[j] ends
    # with the j-th character of the sorted column, the first one of row j
    start = [0] * (CHARS + 1)
    for c in last:
        start[c + 1] += 1
    for c in range(CHARS):
        start[c + 1] += start[c]
    # seven low bits store ascii; an index below 100000 fits in the remaining bits.
    order = array("I", [0]) * len(last)
    for i, c in enumerate(last):
        order[start[c]] = (i << CHAR_BITS) | c
        start[c] += 1
    text = bytearray(len(last))
    for i in range(len(last)):
        entry = order[row]
        text[i] = entry & (CHARS - 1)
        row = entry >> CHAR_BITS
    sys.stdout.buffer.write(text)
    sys.stdout.buffer.write(b"\n")


main()
