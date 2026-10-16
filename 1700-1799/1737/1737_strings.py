import itertools
import sys

LIMIT = 100000
LETTERS = "abc"


def main():
    n = int(input())
    # a palindrome of two or more letters has one of two or three letters
    # in its middle, so any three letters in a row must differ, and a name
    # is one order of a, b, c repeated
    names = sorted({"".join(p[i % len(p)] for i in range(n))
                    for p in itertools.permutations(LETTERS)})
    if len(names) * n > LIMIT:
        print("TOO LONG")
        return
    sys.stdout.write("\n".join(names) + "\n")


main()
