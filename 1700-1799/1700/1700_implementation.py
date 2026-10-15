import sys


def main():
    lines = sys.stdin.read().split("\n")
    n = int(lines[0])
    known = {}
    for line in lines[1:1 + n]:
        name, _, rest = line.partition(":")
        known[name.strip()] = set(rest.split())
    m = int(lines[1 + n])
    out = []
    for line in lines[2 + n:2 + n + m]:
        # the common associations are the intersection of the sets
        common = set.intersection(*(known[name] for name in line.split()))
        out.append(" ".join(sorted(common)) if common else "No solution.")
    print("\n".join(out))


main()
