"""The input for a given N, for the cases whose expressions are too long
to keep as files."""

import sys


def main():
    sys.stdout.write("%d\n" % int(sys.argv[1]))


if __name__ == "__main__":
    main()
