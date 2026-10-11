import sys

MAX_N = 200
# state i (1 to MAX_N+1) stands on cell i of the minuses; state SEEK+d
# still has to move d cells to the left before reaching the survivor
SEEK = 300
# states that cross the minuses to the right of the survivor, walk back
# over it, cross those to its left and return to it
RIGHT = 600
BACK = 601
LEFT = 602
RETURNED = 603


def main():
    k = int(sys.stdin.read())
    rules = []

    def rule(state, read, nxt, write, move):
        rules.append("%d %s %d %s %s" % (state, read, nxt, write, move))

    # survivor = 0-based position of the minus that stays out of n, by the
    # Josephus recurrence
    survivor = 0
    for n in range(1, MAX_N + 1):
        survivor = (survivor + k) % n
        rule(n, "-", n + 1, "-", ">")
        # the head stands on the # after n minuses and moves onto cell n
        rule(n + 1, "#", SEEK + n - 1 - survivor, "#", "<")
    for d in range(1, MAX_N):
        rule(SEEK + d, "-", SEEK + d - 1, "-", "<")
    rule(SEEK, "-", RIGHT, "-", ">")
    rule(RIGHT, "-", RIGHT, "+", ">")
    rule(RIGHT, "+", RIGHT, "+", ">")
    rule(RIGHT, "#", BACK, "#", "<")
    rule(BACK, "+", BACK, "+", "<")
    rule(BACK, "-", LEFT, "-", "<")
    rule(LEFT, "-", LEFT, "+", "<")
    rule(LEFT, "+", LEFT, "+", "<")
    rule(LEFT, "#", RETURNED, "#", ">")
    rule(RETURNED, "+", RETURNED, "+", ">")
    sys.stdout.write("%d\n%s\n" % (len(rules), "\n".join(rules)))


main()
