import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    row = "".join(data[1:])[:n]
    # a turning pair "><" becomes "<>", a swap of neighbours that removes one
    # pair with '>' before '<', so the count of such pairs is the answer
    right = turns = 0
    for c in row:
        if c == ">":
            right += 1
        elif c == "<":
            turns += right
    print(turns)


main()
