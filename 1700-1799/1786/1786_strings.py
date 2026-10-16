import sys

NAME = "Sandro"
COINS = 5


def cost(a, b):
    # one fee for the wrong case, one for the wrong letter
    return COINS * ((a.isupper() != b.isupper()) + (a.lower() != b.lower()))


def main():
    text = sys.stdin.read().strip()
    print(min(sum(cost(a, b) for a, b in zip(text[start:], NAME))
              for start in range(len(text) - len(NAME) + 1)))


main()
