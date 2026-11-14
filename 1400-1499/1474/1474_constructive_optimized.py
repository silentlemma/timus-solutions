import sys


def main():
    n = int(sys.stdin.buffer.readline())
    write = sys.stdout.buffer.write
    write(f"{n * (n + 2)}\n".encode())
    tokens = [str(i).encode() for i in range(2 * n + 1)]

    hole, direction = n, 1
    for run in range(2 * n + 1):
        length = min(run + 1, n, 2 * n - run + 1)
        # Rising runs slide last, the middle only jumps, and falling runs slide first.
        if run > n:
            hole += direction
            write(b" ")
            write(tokens[hole])
        jumps = length - (run != n)
        if jumps:
            step = 2 * direction
            first = hole + step
            hole += jumps * step
            write(b" ")
            write(b" ".join(map(tokens.__getitem__, range(first, hole + step, step))))
        if run < n:
            hole += direction
            if run:
                write(b" ")
            write(tokens[hole])
        direction = -direction
    write(b"\n")


main()
