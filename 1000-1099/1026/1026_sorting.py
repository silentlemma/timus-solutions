import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    base = sorted(map(int, data[1 : 1 + n]))
    # after the database: the separator, the number of queries, the queries
    rest = data[2 + n :]
    queries = map(int, rest[1 : 1 + int(rest[0])])
    # the i-th smallest element is the i-th element of the sorted database
    sys.stdout.write("".join("%d\n" % base[i - 1] for i in queries))


main()
