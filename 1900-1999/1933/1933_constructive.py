import sys


def build_schedule(cannons):
    size = 2 * cannons + 1
    return [
        [
            0 if row == column else (row + column + size - 1) % size + 1
            for column in range(size)
        ]
        for row in range(size)
    ]


def main():
    cannons = int(sys.stdin.buffer.read())
    for row in build_schedule(cannons):
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
