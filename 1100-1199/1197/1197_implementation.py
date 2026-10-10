import sys

SIDE = 8
JUMPS = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def main():
    data = sys.stdin.read().split()
    out = []
    for square in data[1 : 1 + int(data[0])]:
        col, row = ord(square[0]) - ord("a"), int(square[1]) - 1
        # the knight attacks every square one jump away that is on the board
        out.append(sum(0 <= col + dc < SIDE and 0 <= row + dr < SIDE for dc, dr in JUMPS))
    print("\n".join(map(str, out)))


main()
