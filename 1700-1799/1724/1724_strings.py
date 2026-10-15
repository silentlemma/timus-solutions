import sys

OPEN = "ACGT"


def main():
    data = sys.stdin.buffer.read().split()
    dna = data[0].decode()
    q = int(data[1])
    numbers = iter(data[2:])
    # the stack after each prefix is a tree node: a push makes a new node, a
    # matching close returns to the parent, a wrong close starts a lone node,
    # and a piece is human exactly when it ends on the node it started on
    parent = [-1]
    letter = [""]
    state = [0] * (len(dna) + 1)
    cur = 0
    for i, c in enumerate(dna):
        if c in OPEN:
            parent.append(cur)
            letter.append(c)
            cur = len(parent) - 1
        elif letter[cur] == c.upper():
            cur = parent[cur]
        else:
            parent.append(-1)
            letter.append("")
            cur = len(parent) - 1
        state[i + 1] = cur
    out = []
    for _ in range(q):
        left, right = int(next(numbers)), int(next(numbers))
        out.append("1" if state[left - 1] == state[right] else "0")
    print("".join(out))


main()
