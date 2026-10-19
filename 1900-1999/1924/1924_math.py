import sys


def winner(size):
    total = size * (size + 1) // 2
    return "black" if total % 2 == 0 else "grimy"


if __name__ == "__main__":
    print(winner(int(sys.stdin.buffer.read())))
