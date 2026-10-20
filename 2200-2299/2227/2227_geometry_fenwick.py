import sys

CUT = b"c"
QUERY_FIELDS = 3


def main():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    coordinates = list(map(int, data[2 : 2 * n + 2]))
    x = coordinates[0::2]
    y = coordinates[1::2]
    prefix = [0] * (n + 1)
    total = 0
    for i in range(n):
        j = i + 1 if i + 1 < n else 0
        total += x[i] * y[j] - y[i] * x[j]
        prefix[i + 1] = total
    removed = [0] * (n + 1)
    output = []
    append = output.append
    base = 2 * n + 2
    for query in range(base, base + QUERY_FIELDS * q, QUERY_FIELDS):
        left = int(data[query + 1]) - 1
        right = int(data[query + 2]) - 1
        if left > right:
            left, right = right, left
        part = prefix[right] - prefix[left] + x[right] * y[left] - y[right] * x[left]
        i = right
        while i > left:
            part -= removed[i]
            i &= i - 1
        boundary = i
        i = left
        while i > boundary:
            part += removed[i]
            i &= i - 1
        other = total - part
        if data[query] == CUT:
            if part < other:
                answer, edge = part, left
            else:
                answer, edge = other, right
            # Charge the discarded area to the first edge of its original arc.
            i = edge + 1
            while i <= n:
                removed[i] += answer
                i += i & -i
            total -= answer
        else:
            answer = part if part > other else other
        append("%d.5" % (answer >> 1) if answer & 1 else "%d.0" % (answer >> 1))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
