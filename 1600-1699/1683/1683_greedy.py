import sys


def main():
    n = int(sys.stdin.readline())
    # a fold of x cm needs x <= length - x, so a strip shrinks at best to
    # half its length, rounded up; folding exactly half each time reaches that
    folds = []
    while n > 1:
        folds.append(n // 2)
        n -= n // 2
    print(len(folds))
    print(" ".join(map(str, folds)))


main()
