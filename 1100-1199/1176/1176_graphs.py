import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, a = int(data[0]), int(data[1])
    # the channels still to lay are the missing ones; every planet has as
    # many of them going out as coming in, so they form one Euler circuit
    todo = [[]]
    for i in range(n):
        row = data[2 + i * n : 2 + (i + 1) * n]
        todo.append([j + 1 for j, t in enumerate(row) if t == b"0" and j != i])
    # Hierholzer: walk until stuck, then back up and splice in side loops
    nxt = [0] * (n + 1)
    stack, circuit = [a], []
    while stack:
        v = stack[-1]
        if nxt[v] < len(todo[v]):
            stack.append(todo[v][nxt[v]])
            nxt[v] += 1
        else:
            circuit.append(stack.pop())
    circuit.reverse()
    out = ["%d %d" % (circuit[k], circuit[k + 1]) for k in range(len(circuit) - 1)]
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


main()
