import sys


def main():
    words = iter(sys.stdin.read().split())
    bags = {color: int(next(words)) for color in ("Blue", "Red", "Yellow")}
    k = int(next(words))
    # one reagent from each needed bag, chosen independently
    ways = 1
    for _ in range(k):
        ways *= bags[next(words)]
    print(ways)


main()
