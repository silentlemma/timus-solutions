import sys


def main():
    lines = sys.stdin.buffer.read().split(b"\n")
    n, k, _ = map(int, lines[0].split())
    # removing an item changes the sum by 1..N and replacing one by -N+1..N-1,
    # never by a multiple of N + 1, so similar sets differ modulo N + 1
    out = ["YES"]
    for line in lines[1 : k + 1]:
        items = line.split()
        out.append(str((sum(map(int, items)) - int(items[0])) % (n + 1) + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
