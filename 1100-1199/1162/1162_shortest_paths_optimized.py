from gc import collect
from sys import implementation, stdin, stdout

# These short bounded scans trade JIT code-cache memory for interpreter work.
if implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("off")
BASE = 10
RATE_DIGITS = 2
RATE_SCALE = BASE**RATE_DIGITS
CHUNK_DIGITS = 1000
GC_PERIOD = 8


def scaled(text, places):
    fractional = len(text.partition(".")[2])
    digits = text.lstrip("+").replace(".", "")
    value = 0
    # Small conversions also accept initial precision beyond the int-string cap.
    for offset in range(0, len(digits), CHUNK_DIGITS):
        part = digits[offset : offset + CHUNK_DIGITS]
        value = value * BASE ** len(part) + int(part)
    return value * BASE ** (places - fractional)


def possible():
    n, m, start, text = stdin.readline().split()
    n, m, start = int(n), int(m), int(start) - 1
    places = max(RATE_DIGITS, len(text.partition(".")[2]))
    initial = scaled(text, places)
    if initial == 0:
        return False
    # A walk of at most n edges loses at most n factors of RATE_SCALE.
    reserve = RATE_SCALE**n
    initial *= reserve
    fee_unit = BASE ** (places - RATE_DIGITS) * reserve
    edges = []
    for exchange in range(m):
        a, b, rab, cab, rba, cba = stdin.readline().split()
        a, b = int(a) - 1, int(b) - 1
        edges.append((a, b, scaled(rab, RATE_DIGITS), scaled(cab, RATE_DIGITS) * fee_unit))
        edges.append((b, a, scaled(rba, RATE_DIGITS), scaled(cba, RATE_DIGITS) * fee_unit))
        # Release transient decimal parser objects before they accumulate.
        if (exchange + 1) % GC_PERIOD == 0:
            collect()
    best = [-1] * n
    best[start] = initial
    for _ in range(n):
        after = best.copy()
        changed = False
        for a, b, rate, cost in edges:
            if best[a] >= cost:
                # Every numerator before the nth relaxation is divisible by100.
                got = (best[a] - cost) * rate // RATE_SCALE
                if got > after[b]:
                    after[b] = got
                    changed = True
        best = after
        if best[start] > initial:
            return True
        if not changed:
            return False
    return True


stdout.write(str("YES" if possible() else "NO"))
