CENTS = 100
PEAK = 2 * CENTS
DIAGONAL = 2 * PEAK


def cents(text):
    negative = text.startswith("-")
    whole, _, fraction = text.lstrip("+-").partition(".")
    value = int(whole or "0") * CENTS + int((fraction + "00")[:2])
    return -value if negative else value


a, b = map(cents, input().split())
k = int(input())
# Round each independent peak, choosing the lower integer on an exact tie.
x = max(0, (a + CENTS - 1) // PEAK)
y = max(0, (b + CENTS - 1) // PEAK)
if x + y > k:
    # A capacity-constrained optimum uses all capacity; solve its parabola.
    x = max(0, min(k, (a - b + PEAK * k + PEAK - 1) // DIAGONAL))
    y = k - x
profit = a * x + b * y - CENTS * (x * x + y * y)
print(str(profit // CENTS) + "." + str(profit % CENTS).zfill(2))
print(x, y)
