import sys

MAX_SALARY = 10**9


def solve(statements, people):
    parent = [-1] * people
    offset = [0] * people
    lower = [0] * people
    upper = [MAX_SALARY] * people
    upper[0] = 0

    def find(v):
        total = 0
        while parent[v] >= 0:
            p = parent[v]
            grandparent = parent[p]
            if grandparent >= 0:
                offset[v] += offset[p]
                parent[v] = grandparent
            total += offset[v]
            v = parent[v]
        return v, total

    for i, statement in enumerate(statements, 1):
        a, b, difference = map(int, statement.split())
        left, left_offset = find(a)
        right, right_offset = find(b)
        shift = left_offset - right_offset - difference
        if left == right:
            if shift:
                return i, None
            continue
        if parent[left] > parent[right]:
            left, right, shift = right, left, -shift
        right_lower = lower[right] - shift
        right_upper = upper[right] - shift
        if right_lower > lower[left]:
            lower[left] = right_lower
        if right_upper < upper[left]:
            upper[left] = right_upper
        if lower[left] > upper[left]:
            return i, None
        parent[left] += parent[right]
        parent[right] = left
        offset[right] = shift

    def salaries():
        for v in range(people):
            root, delta = find(v)
            yield str(lower[root] + delta)

    return 0, salaries()


def main():
    stream = sys.stdin.buffer
    people, count = map(int, stream.readline().split())
    statements = (stream.readline() for _ in range(count))
    failure, salaries = solve(statements, people)
    if failure:
        print(f"Impossible after {failure} statements")
    else:
        print("Possible")
        print("\n".join(salaries))


if __name__ == "__main__":
    main()
