import sys


def main():
    words = iter(sys.stdin.read().split())
    menu = {next(words) for _ in range(int(next(words)))}
    k = int(next(words))
    blocks = [{next(words) for _ in range(int(next(words)))} for _ in range(k + 1)]
    m = int(next(words))
    # the first student was fine, so the meal is m products of the rest
    safe = menu - blocks[0]
    out = []
    for danger in blocks[1:]:
        if m == 0 or not safe & danger:
            out.append("YES")
        elif len(safe - danger) < m:
            out.append("NO")  # every possible meal holds a dangerous product
        else:
            out.append("MAYBE")
    print("\n".join(out))


main()
