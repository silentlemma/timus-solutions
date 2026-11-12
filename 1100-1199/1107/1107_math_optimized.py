import sys


def main():
    read = sys.stdin.buffer.readline
    n, sets, _ = map(int, read().split())
    divisor = n + 1
    output = bytearray(b"YES\n")
    for _ in range(sets):
        values = map(int, read().split())
        next(values)
        output.extend(f"{sum(values) % divisor + 1}\n".encode())
    sys.stdout.buffer.write(output)


main()
