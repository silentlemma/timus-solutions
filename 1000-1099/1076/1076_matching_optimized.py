from sys import stdin

INFINITY = 1 << 20


def maximum_saved(rows):
    n = len(rows)
    # Each row starts with a feasible potential and a zero reduced cost at its maximum.
    row_price = [0] + [-max(row) for row in rows]
    col_price = [0] * (n + 1)
    owner = [0] * (n + 1)
    unmatched = []
    for row_id, row in enumerate(rows, 1):
        maximum = -row_price[row_id]
        for col, amount in enumerate(row, 1):
            if amount == maximum and owner[col] == 0:
                owner[col] = row_id
                break
        else:
            unmatched.append(row_id)

    previous = [0] * (n + 1)
    for row_id in unmatched:
        owner[0] = row_id
        col = 0
        distance = [INFINITY] * (n + 1)
        remaining = list(range(1, n + 1))
        visited = []
        while True:
            visited.append(col)
            r = owner[col]
            amounts, price = rows[r - 1], row_price[r]
            delta, best, free = INFINITY, 0, False
            for pos, j in enumerate(remaining):
                reduced = -amounts[j - 1] - price - col_price[j]
                if reduced < distance[j]:
                    distance[j], previous[j] = reduced, col
                slack = distance[j]
                if slack < delta or (slack == delta and not free and owner[j] == 0):
                    delta, best, free = slack, pos, owner[j] == 0
            if delta:
                for j in visited:
                    row_price[owner[j]] += delta
                    col_price[j] -= delta
                for j in remaining:
                    distance[j] -= delta
            col = remaining[best]
            if free:
                break
            remaining[best] = remaining[-1]
            remaining.pop()
        while col:
            prior = previous[col]
            owner[col] = owner[prior]
            col = prior
    return sum(rows[owner[col] - 1][col - 1] for col in range(1, n + 1))


def main():
    data = iter(map(int, stdin.buffer.read().split()))
    n = next(data)
    rows = [bytes(next(data) for _ in range(n)) for _ in range(n)]
    print(sum(map(sum, rows)) - maximum_saved(rows))


if __name__ == "__main__":
    main()
