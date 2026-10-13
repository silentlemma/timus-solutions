import sys

LONGEST = 30
DIGITS = (1, 2)
BASE = 10


def main():
    n = int(sys.stdin.read())
    # breadth-first search over remainders: shorter numbers come first, and
    # within one length the queue keeps numeric order, so the first number
    # to reach a remainder is the smallest (parent -2: unseen, -1: one digit)
    parent = [-2] * n
    digit = [0] * n
    length = [0] * n
    queue = []
    for d in DIGITS:
        r = d % n
        if parent[r] == -2:
            parent[r], digit[r], length[r] = -1, d, 1
            queue.append(r)
    head = 0
    while head < len(queue) and parent[0] == -2:
        r = queue[head]
        head += 1
        if length[r] == LONGEST:
            continue
        for d in DIGITS:
            s = (r * BASE + d) % n
            if parent[s] == -2:
                parent[s], digit[s], length[s] = r, d, length[r] + 1
                queue.append(s)
    if parent[0] == -2:
        print("Impossible")
        return
    out = []
    r = 0
    while r != -1:
        out.append(str(digit[r]))
        r = parent[r]
    print("".join(reversed(out)))


main()
