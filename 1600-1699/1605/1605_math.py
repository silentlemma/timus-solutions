import math


def main():
    n = int(input())
    # x_n = 2/3 - (-1)^n (2/3) 2^-n: an even n leaves k sixes while
    # 10^k <= 2^n, an odd n while 2 10^k < 2^n, that is 10^k <= 2^(n-1)
    m = n if n % 2 == 0 else n - 1
    print(math.floor(m * math.log10(2)))


main()
