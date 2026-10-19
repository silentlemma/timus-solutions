import sys


DIAGONAL_WEIGHT = 2
PAIR_WEIGHT = 3
NORMALIZER = 27


def expectation_fraction(vertices):
    origin_x, origin_y = vertices[0]
    previous_x = vertices[1][0] - origin_x
    previous_y = vertices[1][1] - origin_y
    doubled_area = 0
    numerator = 0
    weighted_x = weighted_y = 0
    for x, y in vertices[2:]:
        x -= origin_x
        y -= origin_y
        area = previous_x * y - previous_y * x
        sum_x, sum_y = previous_x + x, previous_y + y
        between = weighted_x * sum_y - weighted_y * sum_x
        numerator += DIAGONAL_WEIGHT * area * area * area + PAIR_WEIGHT * area * between
        weighted_x += area * sum_x
        weighted_y += area * sum_y
        doubled_area += area
        previous_x, previous_y = x, y
    return numerator, NORMALIZER * doubled_area * doubled_area


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(tokens)
    vertices = [(next(tokens), next(tokens)) for _ in range(count)]
    numerator, denominator = expectation_fraction(vertices)
    print(f'{numerator / denominator:.12f}')


if __name__ == '__main__':
    main()
