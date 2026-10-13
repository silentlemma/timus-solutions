import bisect
import sys

LIMIT = 20
INDENT = "  "


def main():
    names = ["sun"]  # the base starts with this one name
    known = set(names)
    out = []
    for line in sys.stdin.read().split():
        op, arg = line[0], line[1:]
        if op == "+":
            if arg not in known:
                known.add(arg)
                bisect.insort(names, arg)
            continue
        out.append(arg)
        # names with this prefix form a run starting where the prefix would go
        i = bisect.bisect_left(names, arg)
        for name in names[i : i + LIMIT]:
            if not name.startswith(arg):
                break
            out.append(INDENT + name)
    sys.stdout.write("".join(line + "\n" for line in out))


main()
