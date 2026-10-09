import sys


def show(folder, depth, out):
    # subfolders are sorted by name, not as parts of a full path
    for name in sorted(folder):
        out.append(" " * depth + name)
        show(folder[name], depth + 1, out)


def main():
    tok = sys.stdin.read().split()
    n = int(tok[0])
    root = {}
    for path in tok[1 : n + 1]:
        cur = root
        for name in path.split("\\"):
            cur = cur.setdefault(name, {})
    out = []
    show(root, 0, out)
    sys.stdout.write("\n".join(out) + "\n")


main()
