import sys

PLAYERS = 3


def main():
    words = iter(sys.stdin.buffer.read().split())
    common = None
    for _ in range(PLAYERS):
        own = {int(next(words)) for _ in range(int(next(words)))}
        common = own if common is None else common & own
    print(len(common))


main()
