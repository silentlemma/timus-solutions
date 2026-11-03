from sys import stdin, stdout

# These short bounded scans trade JIT code-cache memory for interpreter work.
import pypyjit

pypyjit.set_param("off")

QUARTERS = 4


r = int(stdin.read())
y, total = r, 0
radius_squared = r * r
# In column x, exactly y nearest corners lie strictly inside the disc.
# The boundary moves down at most r times over the whole scan.
for x in range(r):
    square = x * x
    while y > 0 and square + (y - 1) * (y - 1) >= radius_squared:
        y -= 1
    total += y
stdout.write(str(QUARTERS * total))
