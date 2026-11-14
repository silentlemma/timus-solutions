def can_collapse(mana, height, top, x, y, ax, ay, bx, by, cx, cy, tx, ty):
    radius = mana - height
    if radius <= 0:
        return False
    if radius >= height:
        return True

    radius_squared = radius * radius
    for sx, sy, ex, ey in ((ax, ay, bx, by), (bx, by, cx, cy), (cx, cy, ax, ay)):
        ux, uy = ex - sx, ey - sy
        nx, ny = uy * top, -ux * top
        nz = ux * (ty - sy) - uy * (tx - sx)
        reach = nx * (x - sx) + ny * (y - sy) + nz * height
        if reach * reach <= radius_squared * (nx * nx + ny * ny + nz * nz):
            return True
    return False


if __name__ == "__main__":
    with open(0, "rb") as source:
        possible = can_collapse(*map(int, source.read().split()))
    print("YES" if possible else "NO")
