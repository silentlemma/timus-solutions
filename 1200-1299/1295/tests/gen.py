"""n: a seed. Any n from 1 to 300000."""

import random
import sys

TOP = 300000


def main():
    print(random.Random(int(sys.argv[1])).randint(1, TOP))


if __name__ == "__main__":
    main()
