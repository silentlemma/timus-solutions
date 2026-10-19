import sys

BASE = 10
LIMIT = BASE * BASE - 1
TURN = "01????9?86"


def solve(count):
    run = 0
    for value in range(1, LIMIT + 1):
        if TURN[value // BASE] != "?" and TURN[value % BASE] != "?":
            run += 1
        else:
            run = 0
        if run >= count:
            return " ".join(
                TURN[target % BASE] + TURN[target // BASE]
                for target in range(value, value - count, -1)
            )
    return "Glupenky Pierre"


def main():
    data = sys.stdin.buffer.read()
    if data:
        print(solve(int(data)))


if __name__ == "__main__":
    main()
