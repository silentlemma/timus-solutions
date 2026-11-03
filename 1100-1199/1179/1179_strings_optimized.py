import sys

DIGITS = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WALL = len(DIGITS)
SMALLEST = 2
BYTES = 256
CHUNK = 1 << 14


def main():
    table = bytearray([WALL]) * BYTES
    for value, char in enumerate(DIGITS):
        table[char] = value
    change = [0] * (WALL + 2)
    left = WALL
    while data := sys.stdin.buffer.read(CHUNK):
        for right in data.translate(table):
            if right < left:
                first = right + 1
                if first < SMALLEST:
                    first = SMALLEST
                change[first] += 1
                change[left + 1] -= 1
            left = right
    best_base, best, running = SMALLEST, -1, 0
    for base in range(SMALLEST, WALL + 1):
        running += change[base]
        if running > best:
            best_base, best = base, running
    print(best_base, best)


main()
