import sys

# where the cheapest way to an office comes from
START = 0
BELOW = 1
LEFT = 2
RIGHT = 3


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    m, n = data[0], data[1]
    best, frm = [], []
    for i in range(m):
        fee = data[2 + i * n : 2 + (i + 1) * n]
        # from below first, then improve along the floor in both directions
        if i == 0:
            row, how = list(fee), [START] * n
        else:
            row, how = [f + b for f, b in zip(fee, best[-1])], [BELOW] * n
        for j in range(1, n):
            if row[j - 1] + fee[j] < row[j]:
                row[j], how[j] = row[j - 1] + fee[j], LEFT
        for j in range(n - 2, -1, -1):
            if row[j + 1] + fee[j] < row[j]:
                row[j], how[j] = row[j + 1] + fee[j], RIGHT
        best.append(row)
        frm.append(how)
    i, j = m - 1, min(range(n), key=best[-1].__getitem__)
    # walk the choices back to the first floor, then print them in order
    rooms = [j + 1]
    while frm[i][j] != START:
        step = frm[i][j]
        if step == BELOW:
            i -= 1
        else:
            j += -1 if step == LEFT else 1
        rooms.append(j + 1)
    print(*reversed(rooms))


main()
