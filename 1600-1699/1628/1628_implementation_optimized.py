import sys
from bisect import bisect_left


INPUT_BUFFER = 4096


def numbers():
    # carry only an unfinished token across refills, even when a line is huge.
    pending = b""
    for chunk in iter(lambda: sys.stdin.buffer.read(INPUT_BUFFER), b""):
        data = pending + chunk
        tokens = data.split()
        pending = tokens.pop() if data[-1] > ord(" ") else b""
        for token in tokens:
            yield int(token)
    if pending:
        yield int(pending)


def main():
    values = numbers()
    m, n, k = next(values), next(values), next(values)
    stride, column_stride = n + 2, m + 2
    # row-major keys replace coordinate tuples; dimensions are at most 30000.
    rows, columns = [], []
    for _ in range(k):
        x, y = next(values), next(values)
        rows.append(x * stride + y)
        columns.append(y * column_stride + x)
    rows.sort()
    columns.sort()

    def contains(key):
        index = bisect_left(rows, key)
        return index < k and rows[index] == key

    answer = at = 0
    for x in range(1, m + 1):
        previous = 0
        while True:
            if at < k and rows[at] // stride == x:
                following = rows[at] % stride
                at += 1
            else:
                following = n + 1
            length = following - previous - 1
            cell = x * stride + previous + 1
            if length >= 2 or (
                length == 1
                and (x == 1 or contains(cell - stride))
                and (x == m or contains(cell + stride))
            ):
                answer += 1
            if following == n + 1:
                break
            previous = following
    at = 0
    for y in range(1, n + 1):
        previous = 0
        while True:
            if at < k and columns[at] // column_stride == y:
                following = columns[at] % column_stride
                at += 1
            else:
                following = m + 1
            answer += following - previous - 1 >= 2
            if following == m + 1:
                break
            previous = following
    print(answer)


main()
