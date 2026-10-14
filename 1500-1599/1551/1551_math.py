import sys
from collections import Counter


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    largest = max(Counter(words[2::2]).values())
    # c wrestlers of one prefecture can avoid each other in all rounds but
    # ceil(log2 c) of them, and dealing the wrestlers sorted by prefecture
    # round-robin into that many top-level groups achieves it for all at once
    unsafe = 0
    while 1 << unsafe < largest:
        unsafe += 1
    print(n - unsafe)


main()
