import math
import sys

OUTPUT_DIGITS = 10


def radius(count):
    if count == 1:
        return 1.0
    return 1.0 + 1.0 / math.sin(math.pi / count)


def main():
    count = int(sys.stdin.buffer.read())
    print(f"{radius(count):.{OUTPUT_DIGITS}f}")


if __name__ == "__main__":
    main()
