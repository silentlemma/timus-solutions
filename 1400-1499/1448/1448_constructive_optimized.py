import sys

PERCENT = 100
PERIODS_PER_BLOCK = 80
OFF = ord("0")


def main():
    count, brightness = map(int, sys.stdin.buffer.read().split())
    period = bytes(
        OFF + (i + 1) * brightness // PERCENT - i * brightness // PERCENT for i in range(PERCENT)
    )
    block = period * PERIODS_PER_BLOCK
    blocks, tail = divmod(count, len(block))
    write = sys.stdout.buffer.write
    for _ in range(blocks):
        write(block)
    write(block[:tail])
    write(b"\n")


if __name__ == "__main__":
    main()
