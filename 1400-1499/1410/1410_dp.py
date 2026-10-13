import re
import sys


def main():
    words = re.findall(rb"[A-Za-z]+", sys.stdin.buffer.read())
    # best sums with the last word kept and dropped; neighbours may not both stay
    kept = dropped = 0
    for word in words:
        kept, dropped = dropped + len(word), max(kept, dropped)
    print(max(kept, dropped))


main()
