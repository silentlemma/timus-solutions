from math import pi, sqrt

MIN_ROPE = 1.0
MAX_ROPE = 50.0
MIN_SEPARATION = 2 * MIN_ROPE
EPS = 1e-9


def rope_limits(points):
    limits = []
    for i, (x, y) in enumerate(points):
        cap = MAX_ROPE * MAX_ROPE
        # Once the horizontal gap reaches the cap, later trees cannot lower it.
        for step in (-1, 1):
            j = i + step
            while 0 <= j < len(points):
                other_x, other_y = points[j]
                dx = x - other_x
                horizontal = dx * dx
                if horizontal >= cap:
                    break
                dy = y - other_y
                squared = horizontal + dy * dy
                if squared < cap:
                    cap = squared
                j += step
        limits.append((cap, sqrt(cap), x, y))
    return sorted(limits, reverse=True)


def maximum(points):
    trees = rope_limits(sorted(points))
    best = 0.0
    for i, (square_a, a, x, y) in enumerate(trees[:-1]):
        if square_a + trees[i + 1][0] <= best:
            break
        for j in range(i + 1, len(trees)):
            square_b, b, other_x, other_y = trees[j]
            upper = square_a + square_b
            if upper <= best or b < MIN_ROPE - EPS:
                break
            dx, dy = x - other_x, y - other_y
            squared = dx * dx + dy * dy
            total = a + b
            if squared >= total * total:
                best = upper
                break
            if squared < MIN_SEPARATION * MIN_SEPARATION - EPS:
                continue
            distance = sqrt(squared)
            long_a = min(a, distance - MIN_ROPE)
            long_b = min(b, distance - MIN_ROPE)
            short_a, short_b = distance - long_b, distance - long_a
            best = max(
                best, long_a * long_a + short_b * short_b, short_a * short_a + long_b * long_b
            )
    return pi * best


def main():
    data = iter(open(0).read().split())
    n = int(next(data))
    points = [(float(next(data)), float(next(data))) for _ in range(n)]
    print(f"{maximum(points):.4f}")


if __name__ == "__main__":
    main()
