import sys

NEW, PATH, GOOD = 0, 1, 2


def consistent(names):
    if names.count(0) != 1:
        return False
    state = [NEW] * (len(names) + 1)
    for start in range(1, len(names) + 1):
        # follow the accusations until a confessor or a child already known
        # to lead to one; meeting the current path again means a ring
        path, v = [], start
        while v != 0 and state[v] == NEW:
            state[v] = PATH
            path.append(v)
            v = names[v - 1]
        if v != 0 and state[v] == PATH:
            return False
        for u in path:
            state[u] = GOOD
    return True


def main():
    data = sys.stdin.buffer.read().split()
    t, pos, out = int(data[0]), 1, []
    for _ in range(t):
        n = int(data[pos])
        names = list(map(int, data[pos + 1 : pos + 1 + n]))
        pos += 1 + n
        out.append("YES" if consistent(names) else "NO")
    print("\n".join(out))


main()
