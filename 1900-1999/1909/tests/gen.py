import random
import sys

MAX_COORDINATE = 100000


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def clear(case):
    center, radius, first, second, velocity = case
    edge = tuple(b - a for a, b in zip(first, second))
    left = tuple(a - c for a, c in zip(first, center))
    if not any(velocity) or not any(edge):
        return False
    length = dot(edge, edge)
    projection = dot(left, edge)
    if projection >= 0:
        return dot(left, left) > radius * radius
    if projection <= -length:
        right = tuple(b - c for b, c in zip(second, center))
        return dot(right, right) > radius * radius
    return dot(left, left) * length - projection * projection > radius * radius * length


def main():
    randomizer = random.Random(int(sys.argv[1]))
    mode = int(sys.argv[2])
    origin = (0, 0, 0)
    if mode in (1, 2):
        bound = 10 if mode == 1 else MAX_COORDINATE
        while True:
            center, first, second, velocity = [
                tuple(randomizer.randint(-bound, bound) for _ in range(3))
                for _ in range(4)
            ]
            radius = randomizer.randint(1, bound)
            case = center, radius, first, second, velocity
            if clear(case):
                break
    elif mode == 3:
        radius = randomizer.randint(1, MAX_COORDINATE)
        case = (
            origin,
            radius,
            (-MAX_COORDINATE, -MAX_COORDINATE, radius),
            (-MAX_COORDINATE, MAX_COORDINATE, radius),
            (randomizer.randint(1, MAX_COORDINATE), 0, 0),
        )
    elif mode in (4, 5, 6):
        radius = randomizer.randint(3, MAX_COORDINATE // 2)
        shift = 0 if mode == 4 else -1 if mode == 5 else 1
        speed = randomizer.randint(1, MAX_COORDINATE)
        case = (
            origin,
            radius,
            (-2 * radius, -radius + shift, 0),
            (-2 * radius, radius + shift, 0),
            (speed, speed, 0),
        )
    elif mode == 7:
        radius = randomizer.randint(1, MAX_COORDINATE // 2)
        case = origin, radius, (-radius - 2, 0, 0), (-radius - 1, 0, 0), (1, 0, 0)
    elif mode == 8:
        case = (1, 0, 0), 1, (-100000, -100000, 0), (0, -1, 0), (99999, 99998, 0)
    elif mode == 9:
        case = (
            (0, 0, -1),
            MAX_COORDINATE,
            (-MAX_COORDINATE, -MAX_COORDINATE, MAX_COORDINATE),
            (-MAX_COORDINATE, MAX_COORDINATE, MAX_COORDINATE),
            (MAX_COORDINATE, 0, 0),
        )
    elif mode == 10:
        radius = randomizer.randint(2, MAX_COORDINATE // 2)
        case = origin, radius, (-2 * radius, -1, 0), (-2 * radius, 1, 0), (1, 0, 0)
    elif mode == 11:
        while True:
            first, second, velocity = [
                tuple(randomizer.randint(-10, 10) for _ in range(3)) for _ in range(3)
            ]
            radius = 2
            case = origin, radius, first, second, velocity
            edge = tuple(b - a for a, b in zip(first, second))
            projection = dot(first, edge)
            if (
                clear(case)
                and (dot(first, first) - radius * radius) * dot(edge, edge)
                < projection**2
            ):
                break
    else:
        while True:
            first, second = [
                tuple(randomizer.randint(-1000, 1000) for _ in range(3))
                for _ in range(2)
            ]
            radius = randomizer.randint(1, 300)
            edge = tuple(b - a for a, b in zip(first, second))
            velocity = (-edge[1], edge[0], 0)
            case = origin, radius, first, second, velocity
            if clear(case):
                break
    assert clear(case)
    center, radius, first, second, velocity = case
    assert all(
        abs(value) <= MAX_COORDINATE
        for vector in (center, first, second, velocity)
        for value in vector
    )
    print(*center, radius)
    print(*first)
    print(*second)
    print(*velocity)


if __name__ == "__main__":
    main()
