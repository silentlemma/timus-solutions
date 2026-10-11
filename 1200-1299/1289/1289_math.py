import sys


def main():
    half = int(sys.stdin.read().split()[0]) // 2
    # 1 + 9 k^2 with k = 11...1 (half ones), and 9 k^2 = k 10^half - k
    if half == 0:
        print(1)
    elif half == 1:
        print(10)
    else:
        print("1" * (half - 1) + "0" + "8" * (half - 2) + "90")


main()
