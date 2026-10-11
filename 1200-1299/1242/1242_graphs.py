import sys


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    blood = words.index("BLOOD")
    pairs = list(map(int, words[1:blood]))
    victims = list(map(int, words[blood + 1 :]))
    parents = [[] for _ in range(n + 1)]
    children = [[] for _ in range(n + 1)]
    for child, parent in zip(pairs[::2], pairs[1::2]):
        parents[child].append(parent)
        children[parent].append(child)
    cleared = [False] * (n + 1)
    for v in victims:
        cleared[v] = True
    # the werewolf spares its ancestors and descendants, so no ancestor and
    # no descendant of a victim can be the werewolf
    for links in (parents, children):
        stack, seen = victims[:], [False] * (n + 1)
        while stack:
            for u in links[stack.pop()]:
                if not seen[u]:
                    seen[u] = cleared[u] = True
                    stack.append(u)
    suspects = [str(u) for u in range(1, n + 1) if not cleared[u]]
    print(" ".join(suspects) if suspects else 0)


main()
