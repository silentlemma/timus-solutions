import sys

SOURCE, TARGET, SPARE = b"123"


def position(rods):
    source, target, spare = SOURCE, TARGET, SPARE
    moves = 0
    for rod in reversed(rods):
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
    # Rod numbers are single ASCII digits. Whitespace only separates tokens.
    _, rods = sys.stdin.buffer.read().split(None, 1)
    print(position(rods.translate(None, b" \t\r\n\v\f")))


if __name__ == "__main__":
    main()
