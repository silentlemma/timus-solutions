DIGITS = 6
SCALE = 10**DIGITS

h, t, v, x = map(int, input().split())
excess = h - t * x
if excess < 0:
    excess = 0
least = (excess * SCALE + (v - x) // 2) // (v - x)
most = (h * SCALE + x // 2) // x
if most > t * SCALE:
    most = t * SCALE
# Emit integer parts directly: no generic percent formatter or joined result.
print(
    least // SCALE,
    ".",
    str(least % SCALE).zfill(DIGITS),
    " ",
    most // SCALE,
    ".",
    str(most % SCALE).zfill(DIGITS),
    sep="",
)
