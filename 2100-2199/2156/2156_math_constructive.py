import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:n + 1]))
    # Around the circle the rises and the falls cancel out, so the
    # conversations where the next friend is less interesting sum to the same
    # as those where the next one is more interesting; equal neighbours add 0.
    falls, rises, ties = [], [], []
    for i in range(n):
        following = a[(i + 1) % n]
        if a[i] > following:
            falls.append(i + 1)
        elif a[i] < following:
            rises.append(i + 1)
        else:
            ties.append(i + 1)
    if not falls:
        # every difference is 0: one conversation against all the others
        falls.append(ties.pop())
    rises += ties
    out = ["YES"]
    for part in (falls, rises):
        out.append(str(len(part)))
        out.append(" ".join(map(str, part)))
    print("\n".join(out))


main()
