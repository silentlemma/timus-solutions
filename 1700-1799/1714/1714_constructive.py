import sys

HEAD = "aabab"
BLOCK = "bbaaba"  # each block forces two more palindromes
# the end after the blocks for each remainder of n mod 6
TAILS = {5: "", 0: "b", 1: "bb", 2: "bbaaababb", 3: "bbaa", 4: "bbaab"}
# short lengths where the pattern is not yet the best, found by search
SPECIAL = {2: "ab", 8: "aababbaa", 11: "aababbaabab"}


def main():
    n = int(sys.stdin.read())
    if n in SPECIAL:
        print(SPECIAL[n])
    elif n <= len(HEAD):
        print(HEAD[:n])
    else:
        tail = TAILS[n % len(BLOCK)]
        print(HEAD + BLOCK * ((n - len(HEAD) - len(tail)) // len(BLOCK)) + tail)


main()
