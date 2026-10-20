import sys


BLACK = ord("#")
DISPLAY = bytes.maketrans(bytes((0, 1, 2)), b".##")


def main():
    data = iter(sys.stdin.buffer.read().split())
    n = int(next(data))
    m = int(next(data))
    limit = int(next(data))
    height = int(next(data))
    width = int(next(data))
    offsets = []
    for row in range(height):
        pattern = next(data)
        base = row * m
        offsets.extend(base + col for col in range(width) if pattern[col] == BLACK)

    board = bytearray(n * m)
    placements = bytearray(n * m)
    repainted = 0
    count = int(next(data))
    if offsets:
        for step in range(1, count + 1):
            row = int(next(data)) - 1
            col = int(next(data)) - 1
            base = row * m + col
            # After two uses, every black cell of this placement is already repainted.
            if placements[base] == 2:
                continue
            placements[base] += 1
            for offset in offsets:
                cell = base + offset
                state = board[cell]
                if state == 0:
                    board[cell] = 1
                elif state == 1:
                    board[cell] = 2
                    repainted += 1
                    if repainted == limit:
                        print(f"Wasted after stamp #{step}")
                        return

    painted = board.translate(DISPLAY)
    output = b"\n".join(painted[start : start + m] for start in range(0, n * m, m))
    sys.stdout.buffer.write(output + b"\n")


if __name__ == "__main__":
    main()
