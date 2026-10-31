def closure(links, victims):
    seen = pending = victims
    while pending:
        lowest = pending & -pending
        pending ^= lowest
        following = links[lowest.bit_length() - 1] & ~seen
        seen |= following
        pending |= following
    return seen


def main():
    words = (word for line in open(0, "rb") for word in line.split())
    n = int(next(words))
    parents, children = [0] * n, [0] * n
    for child in words:
        if child == b"BLOOD":
            break
        child, parent = int(child) - 1, int(next(words)) - 1
        parents[child] |= 1 << parent
        children[parent] |= 1 << child
    victims = 0
    for word in words:
        victims |= 1 << (int(word) - 1)
    # A victim's ancestors and descendants are independently ruled out.
    cleared = closure(parents, victims) | closure(children, victims)
    answer = [str(v + 1) for v in range(n) if not (cleared >> v) & 1]
    print(" ".join(answer) if answer else 0)


main()
