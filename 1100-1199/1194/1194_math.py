import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    # every two hobbits shake hands exactly once, when their groups part,
    # except the married couples, who go home together and never part
    print(n * (n - 1) // 2 - k)


main()
