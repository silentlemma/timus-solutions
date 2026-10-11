from math import isqrt


def strips(n):
    """The row of cell n and its two diagonal strips, from the left and
    from the right; one step across an edge changes exactly one of them."""
    row = isqrt(n - 1) + 1
    place = n - (row - 1) ** 2  # 1 .. 2 row - 1 within the row
    return row, (place + 1) // 2, (2 * row - place + 1) // 2


def main():
    m, n = map(int, input().split())
    print(sum(abs(a - b) for a, b in zip(strips(m), strips(n))))


main()
