THREE = 3
FOUR = 4


def main():
    n = int(input())
    # threes are best: a 4 or more splits into parts with a larger product, and
    # three 2s lose to two 3s; a leftover 1 joins a 3 to make 2 + 2
    if n < FOUR:
        print(n)
        return
    threes, rest = divmod(n, THREE)
    if rest == 1:
        threes, rest = threes - 1, FOUR
    print(THREE**threes * max(rest, 1))


main()
