import sys

SWAPPED = 2  # a single swap changes exactly two places


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    a = data[1:]
    ascending = sorted(a)
    targets = (ascending, ascending[::-1])
    if any(a == t for t in targets):
        print("Nothing to do here")
        return
    # one swap can only fix a line that differs from a sorted one in exactly
    # two places, and then the swap of those two places does it
    for t in targets:
        wrong = [i for i in range(len(a)) if a[i] != t[i]]
        if len(wrong) == SWAPPED:
            i, j = wrong
            if a[i] == t[j] and a[j] == t[i]:
                print("Yes")
                print(i + 1, j + 1)
                return
    print("No hope")


main()
