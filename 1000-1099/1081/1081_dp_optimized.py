from sys import stdin, stdout


def main():
    n, rank = map(int, stdin.read().split())
    total = zero = 1
    for _ in range(n):
        total, zero = total + zero, total
    if rank > total:
        stdout.write(str(-1))
        return
    rank -= 1
    answer = 0
    for _ in range(n):
        answer <<= 1
        if rank >= zero:
            rank -= zero
            answer |= 1
        # Exact reverse Fibonacci counts also force0 immediately after a1.
        total, zero = zero, total - zero
    stdout.write(str(format(answer, f"0{n}b")))


main()
