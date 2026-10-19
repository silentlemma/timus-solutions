import sys


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    n, q, director_salary = int(next(tokens)), int(next(tokens)), int(next(tokens))
    parent = [0] * n
    salary = [director_salary] + [0] * (n - 1)
    size = [1] * n
    for vertex in range(1, n):
        parent[vertex], salary[vertex] = int(next(tokens)), int(next(tokens))
    for vertex in range(n - 1, 0, -1):
        size[parent[vertex]] += size[vertex]

    # Reserve consecutive child blocks; every parent has a smaller number.
    tin, cursor = [1] * n, [2] * n
    for vertex in range(1, n):
        boss = parent[vertex]
        tin[vertex] = cursor[boss]
        cursor[boss] += size[vertex]
        cursor[vertex] = tin[vertex] + 1
    del parent, cursor
    values = [0] * (n + 1)
    for vertex in range(n):
        values[tin[vertex]] = salary[vertex]
    del salary

    linear, constant = [0] * (n + 1), [0] * (n + 1)
    for i in range(1, n + 1):
        difference = values[i] - values[i - 1]
        linear[i] = difference
        constant[i] = difference * (i - 1)
    del values
    for i in range(1, n + 1):
        ancestor = i + (i & -i)
        if ancestor <= n:
            linear[ancestor] += linear[i]
            constant[ancestor] += constant[i]

    def suffix_add(i, amount):
        weighted = amount * (i - 1)
        while i <= n:
            linear[i] += amount
            constant[i] += weighted
            i += i & -i

    def prefix_sum(i):
        coefficient = offset = 0
        at = i
        while at:
            coefficient += linear[at]
            offset += constant[at]
            at -= at & -at
        return coefficient * i - offset

    for _ in range(q):
        kind = next(tokens)
        vertex, threshold, amount = (
            int(next(tokens)),
            int(next(tokens)),
            int(next(tokens)),
        )
        left = tin[vertex]
        if kind == b"employee":
            total, at = 0, left
            while at:
                total += linear[at]
                at -= at & -at
            length = 1
        else:
            length = size[vertex]
            total = prefix_sum(left + length - 1) - prefix_sum(left - 1)
        if total < threshold * length:
            suffix_add(left, amount)
            suffix_add(left + length, -amount)

    # Undo the Fenwick build to recover the final difference array in linear time.
    for i in range(n, 0, -1):
        ancestor = i + (i & -i)
        if ancestor <= n:
            linear[ancestor] -= linear[i]
    for i in range(1, n + 1):
        linear[i] += linear[i - 1]
    sys.stdout.write("\n".join(str(linear[tin[vertex]]) for vertex in range(n)) + "\n")


main()
