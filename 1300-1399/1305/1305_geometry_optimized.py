import sys


def hull(points):
    x, y = next(points)
    min_x = max_x = x
    min_y = max_y = y
    min_s = max_s = x + y
    min_d = max_d = x - y
    for x, y in points:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        diagonal = x + y
        if diagonal < min_s:
            min_s = diagonal
        if diagonal > max_s:
            max_s = diagonal
        diagonal = x - y
        if diagonal < min_d:
            min_d = diagonal
        if diagonal > max_d:
            max_d = diagonal

    corners = (
        (min_s - min_y, min_y),
        (max_d + min_y, min_y),
        (max_x, max_x - max_d),
        (max_x, max_s - max_x),
        (max_s - max_y, max_y),
        (min_d + max_y, max_y),
        (min_x, min_x - min_d),
        (min_x, min_s - min_x),
    )
    distinct = []
    for point in corners:
        if not distinct or distinct[-1] != point:
            distinct.append(point)
    if len(distinct) > 1 and distinct[0] == distinct[-1]:
        distinct.pop()
    return distinct


def main():
    values = (int(word) for line in sys.stdin.buffer for word in line.split())
    next(values)
    sys.stdout.write("".join(f"{x} {y}\n" for x, y in hull(zip(values, values))))


if __name__ == "__main__":
    main()
