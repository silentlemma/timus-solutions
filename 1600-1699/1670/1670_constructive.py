import sys

LEAF, DIRECT, SKEW = 0, 1, 2


def parts(node):
    """The children of the maximal run of nodes of the same kind below and
    including node, in order of position (both kinds of join are
    associative, so the run reads as one node with many children)."""
    kind = node[0]
    out, todo = [], [node]
    while todo:
        cur = todo.pop()
        if cur[0] == kind:
            todo += [cur[2], cur[1]]
        else:
            out.append(cur)
    return out


def show(root):
    """A direct node is a sequence of its parts; a skew node is its parts
    joined by stars from the smallest values up, which the stars put
    last. Built without recursion: the tree can be 10^4 levels deep."""
    out = []
    # ("text", s), ("expr", node) for an expression or a sequence element,
    # ("seq", node) for an operand of a star
    work = [("expr", root)]
    while work:
        what, node = work.pop()
        if what == "text":
            out.append(node)
        elif node[0] == LEAF:
            out.append(str(node[1]) if what == "expr" else "(%d)" % node[1])
        elif node[0] == SKEW:
            items = []
            for child in reversed(parts(node)):
                items += [("text", "*"), ("seq", child)]
            work.extend(reversed(items[1:]))
        else:
            items = []
            for child in parts(node):
                items += [("text", ","), ("expr", child)]
            items[0] = ("text", "(")
            work.extend(reversed(items + [("text", ")")]))
    text = "".join(out)
    # a lone number at the top must still be a sequence
    return "(%s)" % text if root[0] == LEAF else text


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    perm = [int(w) for w in data[1:1 + n]]
    # blocks of consecutive positions holding consecutive values, as
    # (lowest value, highest value, tree); two neighbours whose value ranges
    # touch join into one block
    stack = []
    for v in perm:
        lo, hi, node = v, v, (LEAF, v)
        while stack:
            plo, phi, prev = stack[-1]
            if phi + 1 == lo:
                node = (DIRECT, prev, node)
            elif hi + 1 == plo:
                node = (SKEW, prev, node)
            else:
                break
            stack.pop()
            lo, hi = min(lo, plo), max(hi, phi)
        stack.append((lo, hi, node))
    print(show(stack[0][2]) if len(stack) == 1 else "IMPOSSIBLE")


main()
