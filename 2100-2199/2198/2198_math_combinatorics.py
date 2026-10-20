import sys

PADDING = 3
MOD = 1000000007


def main():
    n = int(sys.stdin.buffer.read())
    edges = n - 1
    length = 2 * edges
    inverse = [0] * (length + 2)
    choose = [0] * (length + PADDING)
    inverse[1] = 1
    choose[0] = 1
    for i in range(1, length + 1):
        if i > 1:
            inverse[i] = MOD - (MOD // i) * inverse[MOD % i] % MOD
        choose[i] = choose[i - 1] * (length - i + 1) % MOD * inverse[i] % MOD

    # Contour walks are Dyck paths. Sum the counts whose maximum is at least h.
    # Reflection at levels -1 and h gives this second difference, with width h + 1.
    answer = 0
    for width in range(2, edges + 2):
        for offset in range(width, edges + 2, width):
            index = edges + offset
            answer += choose[index - 1] - 2 * choose[index] + choose[index + 1]
    print(answer % MOD)


if __name__ == "__main__":
    main()
