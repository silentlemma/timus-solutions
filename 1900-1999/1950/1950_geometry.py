import sys

DECIMAL_SCALE = 1000
DECIMAL_PLACES = 3
SIDE = 10 * DECIMAL_SCALE
CUTS = 30
GRID_SCALE = 1 << CUTS
INITIAL_AREA = 50.0


def parse_coordinate(text):
    if text.startswith("+"):
        text = text[1:]
    whole, _, fractional = text.partition(".")
    digits = (fractional + "0" * DECIMAL_PLACES)[:DECIMAL_PLACES]
    return int(whole or "0") * DECIMAL_SCALE + int(digits)


def sign(value):
    return (value > 0) - (value < 0)


def opposite(first, second):
    return (first < 0 < second) or (second < 0 < first)


def area_for_sale(x, y):
    point_x, point_y = x * GRID_SCALE, y * GRID_SCALE
    right = SIDE * GRID_SCALE, 0
    first = 0, 0
    second = SIDE * GRID_SCALE, SIDE * GRID_SCALE
    area = INITIAL_AREA
    answer = 0.0
    for _ in range(CUTS):
        middle = (first[0] + second[0]) // 2, (first[1] + second[1]) // 2
        normal_x = sign(middle[1] - right[1])
        normal_y = -sign(middle[0] - right[0])
        origin_side = -normal_x * right[0] - normal_y * right[1]
        target_side = normal_x * (point_x - right[0]) + normal_y * (point_y - right[1])
        ray_right = x * right[1] - y * right[0]
        ray_middle = x * middle[1] - y * middle[0]
        half = area / 2
        if opposite(ray_right, ray_middle) and (
            opposite(origin_side, target_side) or target_side == 0
        ):
            answer += half
        if target_side == 0:
            break
        first_side = normal_x * (first[0] - right[0]) + normal_y * (first[1] - right[1])
        if (target_side > 0) == (first_side > 0):
            second = right
        else:
            first = right
        right = middle
        area = half
    return answer


def main():
    coordinates = sys.stdin.read().split()
    x, y = map(parse_coordinate, coordinates)
    print(f"{area_for_sale(x, y):.10f}")


if __name__ == "__main__":
    main()
