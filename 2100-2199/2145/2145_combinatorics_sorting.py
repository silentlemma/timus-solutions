import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = sorted(map(int, data[1:n + 1]))
    b = sorted(map(int, data[n + 1:2 * n + 1]))
    p = int(data[2 * n + 1])
    # The i-th weakest student can take any of the problems they can solve,
    # except the i problems already taken by weaker students.
    ways = 1 % p
    solvable = 0
    for i, knowledge in enumerate(a):
        while solvable < n and b[solvable] <= knowledge:
            solvable += 1
        ways = ways * (solvable - i) % p
    print(ways)


main()
