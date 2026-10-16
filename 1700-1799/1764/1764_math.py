from itertools import combinations

ROUTES = 4
# each bridge lies on exactly two of the four routes, one pair per bridge,
# in the input order: Nizhny Novgorod, Kotelnich, Perm, Kazan, Vyatskiye
# Polyany, Sarapul
PAIRS = ((0, 3), (0, 2), (2, 3), (1, 2), (1, 3), (0, 1))


def det(rows):
    """Determinant of a small integer matrix, expanded along the first row."""
    if len(rows) == 1:
        return rows[0][0]
    total = 0
    for j, a in enumerate(rows[0]):
        if a:
            minor = [r[:j] + r[j + 1:] for r in rows[1:]]
            total += (-1) ** j * a * det(minor)
    return total


def main():
    caps = [int(v) for v in input().split()]
    # the constraints a.x <= b: a bridge's two routes share its capacity,
    # and no route carries a negative load
    cons = []
    for (i, j), cap in zip(PAIRS, caps):
        a = [0] * ROUTES
        a[i] = a[j] = 1
        cons.append((a, cap))
    for i in range(ROUTES):
        a = [0] * ROUTES
        a[i] = -1
        cons.append((a, 0))
    # the best plan is a corner where four constraints are tight; each
    # corner is solved exactly by Cramer's rule, as numerators over a
    # common positive denominator
    best_num, best_den, best = -1, 1, None
    for chosen in combinations(cons, ROUTES):
        matrix = [a for a, _ in chosen]
        den = det(matrix)
        if den == 0:
            continue
        nums = []
        for k in range(ROUTES):
            swapped = [row[:k] + [b] + row[k + 1:] for row, (_, b) in zip(matrix, chosen)]
            nums.append(det(swapped))
        if den < 0:
            den, nums = -den, [-v for v in nums]
        if all(sum(x * v for x, v in zip(a, nums)) <= b * den for a, b in cons):
            if sum(nums) * best_den > best_num * den:
                best_num, best_den, best = sum(nums), den, (nums, den)
    nums, den = best
    print(" ".join("%.3f" % (v / den) for v in nums))


main()
