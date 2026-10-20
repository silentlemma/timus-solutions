STEP = 5  # four characters of a pigeon and a separating column


def main():
    n = int(input())
    top = input()
    # halves counts the pigeons that break the pattern with the left half looking
    # left, parity those that break the pattern with even positions looking left,
    # and the two opposite patterns break exactly at the other pigeons
    halves = parity = 0
    for i in range(n):
        left = top[i * STEP] == "<"
        halves += left != (i < n // 2)
        parity += left != (i % 2 == 0)
    print(min(halves, n - halves, parity, n - parity))


main()
