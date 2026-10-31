import sys
from array import array

OUTPUT_BATCH = 1024


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
    n = next(values)
    # coordinates <= 10**9 and indices <= 100000: "i" entries take 4 bytes on the
    # judge's platform, enough for values up to 2^31 - 1.
    left, right = array("i"), array("i")
    for _ in range(n):
        a, b = next(values), next(values)
        left.append(a)
        right.append(b)
    m = next(values)
    index, top = 0, -1
    output = []
    for _ in range(m):
        point = next(values)
        while index < n and left[index] <= point:
            while top >= 0 and right[top] < left[index]:
                top = left[top]
            # an activated interval no longer needs its left endpoint; store its parent.
            left[index] = top
            top = index
            index += 1
        while top >= 0 and right[top] < point:
            top = left[top]
        output.append(str(top + 1 if top >= 0 else -1))
        # flushing batches caps output storage independently of the query count.
        if len(output) == OUTPUT_BATCH:
            sys.stdout.write("\n".join(output) + "\n")
            output.clear()
    if output:
        sys.stdout.write("\n".join(output) + "\n")


main()
