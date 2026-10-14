import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cars = [int(v) for v in data[1 : 1 + n]]
    where = [0] * (n + 1)
    for i, car in enumerate(cars):
        where[car] = i
    # cut 1..n into the fewest runs of numbers that already stand in order, and
    # a new run starts where car v + 1 stands before car v
    run = [0] * (n + 1)
    for car in range(2, n + 1):
        run[car] = run[car - 1] + (where[car] < where[car - 1])
    passes = run[n].bit_length()
    # pass b sends the cars whose run number has bit b set to the right, and like a
    # radix sort from the low bit up, the passes leave the runs in order
    lines = [cars]
    for bit in range(passes):
        left = [car for car in cars if not run[car] >> bit & 1]
        right = [car for car in cars if run[car] >> bit & 1]
        cars = left + right
        lines.append(cars)
    out = [str(passes)] + [" ".join(map(str, line)) for line in lines]
    sys.stdout.write("\n".join(out) + "\n")


main()
