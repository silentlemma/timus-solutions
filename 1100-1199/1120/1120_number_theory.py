import os
from sys import stdout

# This short standalone job trades JIT throughput for bounded startup memory.
try:
    import pypyjit
except ImportError:
    pass
else:
    pypyjit.set_param("off")

FIRST_ODD_DIVISOR = 3

total = int(open(0, "rb", buffering=0).read())
odd_part = total
while odd_part % 2 == 0:
    odd_part //= 2
factors = []
divisor = FIRST_ODD_DIVISOR
while divisor * divisor <= odd_part:
    power = 0
    while odd_part % divisor == 0:
        odd_part //= divisor
        power += 1
    if power:
        factors.append((divisor, power))
    divisor += 2
if odd_part > 1:
    factors.append((odd_part, 1))


def divisors(at, value):
    if at == len(factors):
        yield value
        return
    prime, power = factors[at]
    for _ in range(power + 1):
        yield from divisors(at + 1, value)
        value *= prime


best = 1
for odd in divisors(0, 1):
    for length in (odd, 2 * total // odd):
        if length > best and length * (length + 1) <= 2 * total:
            best = length
print((2 * total // best - best + 1) // 2, best)

# Finish the standalone answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
