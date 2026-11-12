import sys


def main():
    read = sys.stdin.readline
    known = {}
    for _ in range(int(read())):
        name, _, rest = read().partition(":")
        known[name.strip()] = frozenset(map(sys.intern, rest.split()))
    write = sys.stdout.write
    for _ in range(int(read())):
        sets = [known[name] for name in read().split()]
        seed = min(sets, key=len)
        common = set(seed)
        for other in sets:
            if not common:
                break
            if other is not seed:
                common.intersection_update(other)
        write((" ".join(sorted(common)) if common else "No solution.") + "\n")


if __name__ == "__main__":
    main()
