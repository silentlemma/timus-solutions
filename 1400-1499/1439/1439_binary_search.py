import sys


def main():
    data = sys.stdin.buffer.read().split()
    queries = data[2:]
    gone = []  # original numbers of destroyed rooms, sorted
    out = []
    for letter, number in zip(queries[::2], queries[1::2]):
        x = int(number)
        # gone[j] - j <= x holds for a prefix: the rooms gone below room x
        lo, hi = 0, len(gone)
        while lo < hi:
            mid = (lo + hi) // 2
            if gone[mid] - mid <= x:
                lo = mid + 1
            else:
                hi = mid
        original = x + lo
        if letter == b"D":
            gone.insert(lo, original)
        else:
            out.append(original)
    sys.stdout.write("".join("%d\n" % v for v in out))


main()
