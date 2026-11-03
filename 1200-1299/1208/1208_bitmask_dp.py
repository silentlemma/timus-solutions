from sys import stdin

count = int(stdin.readline())
teams = [stdin.readline().split() for _ in range(count)]
clash = [1 << team for team in range(count)]
for team, (a, b, c) in enumerate(teams):
    for other in range(team + 1, count):
        if a in teams[other] or b in teams[other] or c in teams[other]:
            clash[team] |= 1 << other
            clash[other] |= 1 << team
del teams
middle = count // 2
left_all = (1 << middle) - 1
best = [0] * (1 << middle)
for mask in range(1, len(best)):
    bit = mask & -mask
    rest = mask ^ bit
    best[mask] = max(best[rest], 1 + best[rest & ~clash[bit.bit_length() - 1]])


def combine(right, allowed):
    if not right:
        return best[allowed]
    bit = right & -right
    conflicts = clash[bit.bit_length() - 1]
    # Enumerate the right half; the left subset optimum is a table lookup.
    return max(combine(right ^ bit, allowed), 1 + combine(right & ~conflicts, allowed & ~conflicts))


print(combine(((1 << count) - 1) ^ left_all, left_all))
