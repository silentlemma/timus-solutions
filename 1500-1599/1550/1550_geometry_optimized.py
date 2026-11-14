PYRAMID_VOLUME_DIVISOR = 3
PI = 3.141592653589793

h, w, x, y, r = map(float, open(0, "rb").read().split())
height_fraction = (w - 2 * max(abs(x), abs(y))) / w
volume = h * (w * w / PYRAMID_VOLUME_DIVISOR - PI * r * r * height_fraction)
print(f"{volume:.5f}")
