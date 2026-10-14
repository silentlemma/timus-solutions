import sys


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    letter = words[1 + n]
    # the dictionary order is kept, repeated entries are printed every time
    found = [w for w in words[1 : 1 + n] if w[0] == letter]
    if found:
        print("\n".join(found))


main()
