FORBIDDEN = 3
MIN_PARTNER_CHOICES = 2

n = int(open(0, "rb").read())
half = n // 2
if n & 1:
    span = half - 1
    print(n * span if span >= MIN_PARTNER_CHOICES else 0, 0)
else:
    intersecting = half * (n - FORBIDDEN)
    groups = (half - 1, half - 2)
    parallel = half * sum(size for size in groups if size >= MIN_PARTNER_CHOICES)
    print(parallel, intersecting)
