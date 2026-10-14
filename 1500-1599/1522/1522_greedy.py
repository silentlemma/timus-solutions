import sys

MACHINES = 3


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    times = list(map(int, data[1 : 1 + MACHINES * n]))
    a, b, c = times[0::MACHINES], times[1::MACHINES], times[2::MACHINES]
    # machine B never holds the line, so the line behaves like two machines
    # with times a + b and b + c, where Johnson's rule is optimal: toys
    # faster on the first come first, by its time, the rest by the second
    first = [a[i] + b[i] for i in range(n)]
    second = [b[i] + c[i] for i in range(n)]
    early = sorted((i for i in range(n) if first[i] < second[i]), key=first.__getitem__)
    late = sorted(
        (i for i in range(n) if first[i] >= second[i]), key=second.__getitem__, reverse=True
    )
    order = early + late
    done_a = done_b = done_c = 0
    for i in order:
        done_a += a[i]
        done_b = max(done_b, done_a) + b[i]
        done_c = max(done_c, done_b) + c[i]
    print(done_c)
    print(" ".join(str(i + 1) for i in order))


main()
