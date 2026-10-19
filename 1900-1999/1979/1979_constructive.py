import sys

FACE_COUNT = 6
HALF_FACES = 3
BELT_FACES = 4


def rows(n):
    area = n * n
    complement = FACE_COUNT * area + 1
    for r in range(n):
        yield [2 * area + r * n + c + 1 for c in range(n)]
    for r in range(n):
        row = []
        for face in range(BELT_FACES):
            for c in range(n):
                if face < 2:
                    value = face * area + r * n + c + 1
                else:
                    value = complement - ((face - 2) * area + r * n + n - c)
                row.append(value)
        yield row
    for r in range(n):
        yield [complement - (HALF_FACES * area - r * n - n + c + 1) for c in range(n)]


def main():
    n = int(sys.stdin.buffer.readline())
    write = sys.stdout.write
    for row in rows(n):
        write(" ".join(map(str, row)) + "\n")


if __name__ == "__main__":
    main()
