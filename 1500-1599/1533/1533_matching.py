import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heavier = [0] * n  # bit j of heavier[i]: hobbit i is known to outweigh j
    for i in range(n):
        for j in range(n):
            if data[1 + i * n + j] == "1":
                heavier[i] |= 1 << j
    # the weighings are consistent, so the closure is a strict order
    for k in range(n):
        for i in range(n):
            if heavier[i] >> k & 1:
                heavier[i] |= heavier[k]
    lighter = [[j for j in range(n) if heavier[i] >> j & 1] for i in range(n)]
    # by Dilworth, the largest set of incomparable hobbits is n minus a
    # maximum matching between "heavier" copies and "lighter" copies
    match_of = [-1] * n  # the heavier hobbit matched to a lighter one

    def augment(i, seen):
        for j in lighter[i]:
            if not seen[j]:
                seen[j] = True
                if match_of[j] < 0 or augment(match_of[j], seen):
                    match_of[j] = i
                    return True
        return False

    matched = [False] * n
    for i in range(n):
        matched[i] = augment(i, [False] * n)
    # Konig: walk alternating paths from the unmatched heavier copies; the
    # hobbits reached on the heavier side but not on the lighter side form
    # the answer, as everything else is a vertex cover
    left = [not matched[i] for i in range(n)]
    right = [False] * n
    stack = [i for i in range(n) if left[i]]
    while stack:
        i = stack.pop()
        for j in lighter[i]:
            if not right[j]:
                right[j] = True
                owner = match_of[j]
                if owner >= 0 and not left[owner]:
                    left[owner] = True
                    stack.append(owner)
    chosen = [i + 1 for i in range(n) if left[i] and not right[i]]
    print(len(chosen))
    print(" ".join(map(str, chosen)))


main()
