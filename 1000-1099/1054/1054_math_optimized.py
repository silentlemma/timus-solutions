import sys


SOURCE, TARGET, SPARE = b"123"
WHITESPACE = b" \t\r\n\v\f"


def position(rods):
    source, target, spare = SOURCE, TARGET, SPARE
    moves = 0
    for rod in rods[::-1]:
        if rod == target:
            moves = 2 * moves + 1
            source, spare = spare, source
        elif rod == source:
            moves *= 2
            target, spare = spare, target
        else:
            return -1
    return moves


def main():
    _, rods = sys.stdin.buffer.read().split(None, 1)
    print(position(rods.translate(None, WHITESPACE)))


if __name__ == "__main__":
    main()
