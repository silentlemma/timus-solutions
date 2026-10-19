import sys


def vertex_clearance(vertices, other, sign):
    result = float("inf")
    index = 0
    last = len(other) - 1
    for x, y in vertices:
        while index < last and other[index + 1][1] <= y:
            index += 1
        if index == last or other[index][1] == y:
            gap = sign * (other[index][0] - x)
        else:
            ax, ay = other[index]
            bx, by = other[index + 1]
            numerator = (ax - x) * (by - y) + (bx - x) * (y - ay)
            gap = sign * numerator / (by - ay)
        if gap < result:
            result = gap
    return result


def fraction_at(vertices, index, y):
    last = len(vertices) - 1
    while index < last and vertices[index + 1][1] <= y:
        index += 1
    if index == last or vertices[index][1] == y:
        return vertices[index][0], 1, index
    ax, ay = vertices[index]
    bx, by = vertices[index + 1]
    return ax * (by - y) + bx * (y - ay), by - ay, index


def pole_groups(read, count):
    current_y = None
    xs = []
    for _ in range(count):
        x, y = map(int, read().split())
        if current_y is not None and y != current_y:
            yield current_y, xs
            xs = []
        current_y = y
        xs.append(x)
    if current_y is not None:
        yield current_y, xs


def solve(left, right, groups):
    answer = min(vertex_clearance(left, right, 1), vertex_clearance(right, left, -1))
    first = second = 0
    bottom, top = left[0][1], left[-1][1]
    for y, xs in groups:
        if y < bottom or y > top:
            continue
        ln, ld, first = fraction_at(left, first, y)
        rn, rd, second = fraction_at(right, second, y)
        xs.sort()
        previous = None
        previous_scaled = 0
        best = 0.0
        for x in xs:
            scaled_left, scaled_right = x * ld, x * rd
            if scaled_left < ln or scaled_right > rn:
                continue
            gap = (scaled_left - ln) / ld if previous is None else x - previous
            if gap > best:
                best = gap
            previous = x
            previous_scaled = scaled_right
        if previous is not None:
            gap = (rn - previous_scaled) / rd
            if gap > best:
                best = gap
            if best < answer:
                answer = best
    return answer


def main():
    read = sys.stdin.buffer.readline
    left = [tuple(map(int, read().split())) for _ in range(int(read()))]
    right = [tuple(map(int, read().split())) for _ in range(int(read()))]
    print(f"{solve(left, right, pole_groups(read, int(read()))):.12f}")


if __name__ == "__main__":
    main()
