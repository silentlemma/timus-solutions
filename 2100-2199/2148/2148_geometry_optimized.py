DIAMETER_SQUARED = 4
SQUARE_ROOT = 0.5

cx, cy, radius, ax, ay, bx, by = map(int, open(0, "rb").read().split())
wx, wy = ax + bx - 2 * cx, ay + by - 2 * cy
norm = wx * wx + wy * wy
# Equal distances to the center make the bisector's midpoint (A + B) / 2.
if norm <= DIAMETER_SQUARED * radius * radius:
    print("No way")
else:
    scale = radius / norm**SQUARE_ROOT
    print(f"{cx + wx * scale:.9f} {cy + wy * scale:.9f}")
