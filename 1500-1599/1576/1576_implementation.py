import sys

FREE = 6  # calls of up to six seconds cost nothing
MINUTE = 60


def main():
    words = iter(sys.stdin.read().split())
    n1, c1 = int(next(words)), int(next(words))
    n2, t, c2 = int(next(words)), int(next(words)), int(next(words))
    n3 = int(next(words))
    k = int(next(words))
    minutes = 0
    for _ in range(k):
        mm, ss = next(words).split(":")
        seconds = int(mm) * MINUTE + int(ss)
        if seconds > FREE:
            minutes += -(-seconds // MINUTE)  # a started minute counts in full
    print("Basic:     %d" % (n1 + c1 * minutes))
    print("Combined:  %d" % (n2 + c2 * max(0, minutes - t)))
    print("Unlimited: %d" % n3)


main()
