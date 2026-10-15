LIMIT = 100000
BASE = 10


def main():
    n = int(input())
    digits = [0] * LIMIT
    for i in range(1, LIMIT):
        digits[i] = digits[i // BASE] + i % BASE
    # take numbers from the top whenever their digits still fit; the small
    # ones at the end fill any remainder, so the sum always comes out
    chosen = []
    for i in range(LIMIT - 1, 0, -1):
        if n == 0:
            break
        if digits[i] <= n:
            chosen.append(i)
            n -= digits[i]
    print(len(chosen))
    print(" ".join(map(str, chosen)))


main()
