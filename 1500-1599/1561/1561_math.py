import sys

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
WEEK = len(DAYS)
DAY = {name: i for i, name in enumerate(DAYS)}
INVERSE = [0] + [pow(x, WEEK - 2, WEEK) for x in range(1, WEEK)]


def main():
    words = iter(sys.stdin.read().split())
    n = int(next(words))
    sorts = 0
    # rows of an echelon basis over the residues modulo 7: each row is
    # (pivot, coefficients, right side) with a 1 at its first non-zero place
    basis = []
    crazy = False
    out = []

    def reduce(vector, value):
        """Subtract basis rows until no pivot of the basis stays non-zero."""
        for pivot, row, right in basis:
            c = vector[pivot]
            if c:
                end = len(row)  # the row is shorter if sorts appeared after it
                vector[pivot:end] = [
                    (v - c * r) % WEEK for v, r in zip(vector[pivot:end], row[pivot:])
                ]
                value = (value - c * right) % WEEK
        return value

    def amounts():
        """The numbers of a query up to its first weekday, and that weekday."""
        vector = []
        word = next(words)
        while word not in DAY:
            vector.append(int(word) % WEEK)
            word = next(words)
        return vector + [0] * (sorts - len(vector)), DAY[word]

    for _ in range(n):
        kind = next(words)
        if kind == "Add":
            sorts += 1
            continue
        vector, start = amounts()
        if kind == "Learn":
            finish = DAY[next(words)]
            if crazy:
                continue
            value = reduce(vector, finish - start)
            pivot = next((i for i, c in enumerate(vector) if c), None)
            if pivot is None:
                crazy = value != 0
                continue
            scale = INVERSE[vector[pivot]]
            row = [c * scale % WEEK for c in vector]
            basis.append((pivot, row, value * scale % WEEK))
            basis.sort(key=lambda r: r[0])
        elif crazy:
            out.append("Already crazy")
        else:
            value = reduce(vector, 0)
            if any(vector):
                out.append("Don't know")
            else:
                out.append(DAYS[(start - value) % WEEK])
    sys.stdout.write("".join(s + "\n" for s in out))


main()
