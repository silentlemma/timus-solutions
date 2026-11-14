import sys


def main():
    lines = iter(sys.stdin.buffer)
    next(lines)
    write = sys.stdout.write
    for line in lines:
        if not line.strip():
            continue
        k, m = map(int, line.split())
        write("0\n" if m > k else f"{(k - m + 1) / (k + 1):.8f}\n")


if __name__ == "__main__":
    main()
