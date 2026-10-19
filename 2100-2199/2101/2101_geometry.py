import sys

VERTICES = 3
DECIMAL_PLACES = 10
SCALE = 10**DECIMAL_PLACES


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    points = list(zip(values[::2], values[1::2]))
    hole_x, hole_y = points[VERTICES]
    best = 0
    count = 0

    def consider(numerator, denominator):
        nonlocal best, count
        rounded = (numerator * SCALE + denominator // 2) // denominator
        best = max(best, rounded)
        count += 1

    for index in range(VERTICES):
        ax, ay = points[index]
        bx, by = points[(index + 1) % VERTICES]
        cx, cy = points[(index + 2) % VERTICES]
        dx, dy = bx - ax, by - ay
        vx, vy = cx - ax, cy - ay
        hx, hy = hole_x - ax, hole_y - ay
        length = dx * dx + dy * dy
        apex = dx * vx + dy * vy

        # Exclude an exterior altitude and one duplicate family in a right triangle.
        if apex < 0 or apex >= length:
            continue

        position = dx * hx + dy * hy
        area = abs(dx * vy - dy * vx)
        height = abs(dx * hy - dy * hx)
        consider(height * (area - height), area)

        if position < apex:
            consider(area * position * (apex - position), apex * apex)
        elif position > apex:
            gap = length - apex
            consider(area * (length - position) * (position - apex), gap * gap)

    print(f"{best // SCALE}.{best % SCALE:0{DECIMAL_PLACES}d}")
    print(count)


if __name__ == "__main__":
    main()
