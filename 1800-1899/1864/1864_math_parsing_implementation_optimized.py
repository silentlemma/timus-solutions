from os import _exit as _finish_process
import sys as _finish_sys
import sys

MONEY = 100


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, bought = data[0], data[1:]
    # everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
    # litre, friend i paid for bought[i] (n + 1) - total litres of others
    total = sum(bought)
    over = []
    for b in bought:
        paid = b * (n + 1) - total
        over.append(paid if paid > 0 else 0)
    denominator = sum(over)
    sys.stdout.write(" ".join(str(MONEY * x // denominator) for x in over) + "\n")


main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
