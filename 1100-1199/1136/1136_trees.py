import sys

# the tree can be a chain of 3000 members, and so can the recursion
RECURSION_LIMIT = 10000


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    post = [int(x) for x in data[1 : 1 + n]]
    # a binary search tree in lists: the number of node v and its children,
    # -1 for a missing child
    number, left, right = [], [], []
    # read backwards, the odd-session order names every chairman before the
    # members of the wings, so inserting in that order rebuilds the tree
    for value in reversed(post):
        node = len(number)
        number.append(value)
        left.append(-1)
        right.append(-1)
        v = 0
        while node:
            side = left if value < number[v] else right
            if side[v] < 0:
                side[v] = node
                break
            v = side[v]
    out = []

    def speak(v):
        # the even-session order: right wing, left wing, then the chairman
        if v >= 0:
            speak(right[v])
            speak(left[v])
            out.append(number[v])

    if n:
        speak(0)
    print("\n".join(map(str, out)))


sys.setrecursionlimit(RECURSION_LIMIT)
main()
