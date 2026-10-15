import sys


def main():
    n, s = (int(w) for w in sys.stdin.read().split())
    yes = s - 2 * n  # YES takes 3 bytes, NO takes 2
    no = n - yes
    # the first test fails when its answer is NO, any later one when its
    # answer differs from the one before: no / n + (n - 1) * 2 yes no / (n (n - 1))
    print("%.7f" % (no * (2 * yes + 1) / n))


main()
