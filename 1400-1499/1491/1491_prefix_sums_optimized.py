import sys
from array import array

OUTPUT_CHUNK = 1024


def main():
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(tokens)
    # At most(n+1)*10000<=1000010000 coins occur, so signed32bits suffice.
    diff = array("i", [0]) * (n + 2)
    for _ in range(n + 1):
        a, b, amount = next(tokens), next(tokens), next(tokens)
        diff[a] += amount
        diff[b + 1] -= amount
    total = 0
    chunk = []
    for i in range(1, n + 1):
        total += diff[i]
        chunk.append(str(total))
        if len(chunk) == OUTPUT_CHUNK:
            sys.stdout.write(" ".join(chunk) + (" " if i < n else "\n"))
            chunk.clear()
    if chunk:
        sys.stdout.write(" ".join(chunk) + "\n")


main()
