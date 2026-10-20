import sys

SCALE = 1000


def coordinate(token):
    return int(token.replace(b".", b""))


def main():
    data = sys.stdin.buffer
    n = int(data.readline())
    points = [tuple(map(coordinate, data.readline().split())) for _ in range(n)]
    left = (min(x for x, _ in points) + SCALE - 1) // SCALE
    right = max(x for x, _ in points) // SCALE
    if left > right:
        print(0)
        return
    lower = [0] * (right + 1)
    upper = [0] * (right + 1)
    for i, (x, y) in enumerate(points):
        nx, ny = points[(i + 1) % n]
        if x == nx:
            continue
        bottom = x < nx
        if not bottom:
            x, nx, y, ny = nx, x, ny, y
        begin = (x + SCALE - 1) // SCALE
        end = nx // SCALE
        dx = nx - x
        dy = ny - y
        denominator = dx * SCALE
        numerator = y * dx + (begin * SCALE - x) * dy - int(bottom)
        step = dy * SCALE
        target = lower if bottom else upper
        if dy == 0:
            target[begin : end + 1] = [numerator // denominator] * (end - begin + 1)
        else:
            for column in range(begin, end + 1):
                target[column] = numerator // denominator
                numerator += step

    limit = min(right, max(upper))
    mu = [1] * (limit + 1)
    composite = bytearray(limit + 1)
    for prime in range(2, limit + 1):
        if composite[prime]:
            continue
        composite[prime::prime] = b"\x01" * (limit // prime)
        for multiple in range(prime, limit + 1, prime):
            mu[multiple] = -mu[multiple]
        square = prime * prime
        if square <= limit:
            mu[square::square] = [0] * (limit // square)

    # Each divisor removes pairs whose two coordinates share that divisor.
    answer = sum(upper) - sum(lower)
    for divisor in range(2, min(limit, right // 2) + 1):
        sign = mu[divisor]
        if sign:
            begin = ((left + divisor - 1) // divisor) * divisor
            subtotal = sum([value // divisor for value in upper[begin::divisor]])
            subtotal -= sum([value // divisor for value in lower[begin::divisor]])
            answer += sign * subtotal
    # Above half the maximum column, the only column divisible by d is d itself.
    for divisor in range(max(2, left, right // 2 + 1), limit + 1):
        sign = mu[divisor]
        if sign:
            answer += sign * (upper[divisor] // divisor - lower[divisor] // divisor)
    print(answer)


if __name__ == "__main__":
    main()
