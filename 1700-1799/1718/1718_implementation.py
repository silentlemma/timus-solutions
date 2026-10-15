import sys

# test 6 was removed and new tests were added after test 7, which became
# test 6: a failure on old test 7 must now read 6, while an accepted run or
# a failure on old test 6 may change or stay as it was
REMOVED = 6
RENUMBERED = 7
NUMBERED = ("ML", "TL", "WA")


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    must, may = set(), set()
    k = 1
    for _ in range(n):
        name, verdict = words[k], words[k + 1]
        k += 2
        if verdict in NUMBERED:
            test = int(words[k])
            k += 1
            if test == RENUMBERED:
                must.add(name)
            elif test == REMOVED:
                may.add(name)
        elif verdict == "AC":
            may.add(name)
    print(len(must), len(must | may))


main()
