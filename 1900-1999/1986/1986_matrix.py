import sys

PERCENT = 100
SCALE = 1000000
DIGITS = 6


def determinant(matrix):
    n = len(matrix)
    if n == 0:
        return 1
    a = [row[:] for row in matrix]
    previous = 1
    sign = 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for row in range(k + 1, n):
            for col in range(k + 1, n):
                a[row][col] = (a[row][col] * pivot - a[row][k] * a[k][col]) // previous
            a[row][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def expand(recipes):
    names = sorted(recipes)
    bases = sorted({part for recipe in recipes.values() for part in recipe} - set(names))
    a = [
        [PERCENT * (i == j) - recipes[name].get(other, 0) for j, other in enumerate(names)]
        for i, name in enumerate(names)
    ]
    denominator = determinant(a)
    numerators = [[0] * len(bases) for _ in names]
    for col in range(len(names)):
        for base_index, base in enumerate(bases):
            replaced = [row[:] for row in a]
            for row, name in enumerate(names):
                replaced[row][col] = recipes[name].get(base, 0)
            numerators[col][base_index] = determinant(replaced)
    return names, bases, numerators, denominator


def solve(text):
    recipes = {}
    for line in text.splitlines():
        if line.strip():
            name, body = line.split(":", 1)
            tokens = body.split()
            recipes[name.strip()] = dict(zip(tokens[::2], map(int, tokens[1::2])))
    names, bases, numerators, denominator = expand(recipes)
    lines = []
    for name, row in zip(names, numerators):
        units = [value * PERCENT * SCALE // denominator for value in row]
        largest = max(range(len(row)), key=row.__getitem__)
        units[largest] += PERCENT * SCALE - sum(units)
        parts = [
            f"{base} {value // SCALE}.{value % SCALE:0{DIGITS}d}"
            for base, value in zip(bases, units)
        ]
        lines.append(name + " : " + " ".join(parts))
    return "\n".join(lines) + ("\n" if lines else "")


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
