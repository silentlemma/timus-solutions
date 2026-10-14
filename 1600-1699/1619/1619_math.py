import sys


def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # the ballot theorem: the elder stays ahead or level with this chance
        out.append("0" if m > k else "%.10f" % ((k - m + 1) / (k + 1)))
    print("\n".join(out))


main()
